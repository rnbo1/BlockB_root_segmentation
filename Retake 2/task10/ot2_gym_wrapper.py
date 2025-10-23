import gymnasium as gym
from gymnasium import spaces
import numpy as np
from sim_class import Simulation


class OT2Env(gym.Env):
    def __init__(self, render=False, max_steps=1000, threshold=0.001, bonus_reward=0,
                 reward_distance_scale=100, step_penalty=-1):
        super(OT2Env, self).__init__()
        self.render = render
        self.max_steps = max_steps
        self.threshold = threshold
        self.bonus_reward = bonus_reward
        self.reward_distance_scale = reward_distance_scale
        self.step_penalty = step_penalty

        # Create the simulation environment
        self.sim = Simulation(num_agents=1)

        # Define action and observation space
        # They must be gym.spaces objects
        self.action_space = spaces.Box(low=-1, high=1, shape=(3,), dtype=np.float32)
        self.observation_space = spaces.Box(low=np.inf, high=np.inf, shape=(6,), dtype=np.float32)

        # keep track of the number of steps
        self.steps = 0

    def reset(self, seed=None):
        if seed is not None:
            np.random.seed(seed)

        # Reset the environment and get the initial observation
        # Generate a random goal position within bounds
        self.goal_position = np.random.uniform(
            low=[-0.187, -0.1705, 0.1695],
            high=[0.253, 0.2195, 0.2895]
        )

        # Call the environment reset function
        observation = self.sim.reset(num_agents=1)

        # Get the correct robot ID dynamically
        robot_key = list(observation.keys())[0]  # Selects the first available robot ID
        pipette_position = np.array(observation[robot_key]['pipette_position'], dtype=np.float32)

        observation = np.concatenate((pipette_position, self.goal_position)).astype(np.float32)

        self.steps = 0

        return observation, {}  # Now returning a tuple (observation, info)
        
    def step(self, action):
        # Execute one time step within the environment
        scaled_action = np.append(action * 0.5, 0)

        # Call the environment step function
        observation = self.sim.run([scaled_action])

        # Get the correct robot ID dynamically
        robot_key = list(observation.keys())[0]  # Selects the first available robot ID
        pipette_position = np.array(observation[robot_key]['pipette_position'], dtype=np.float32)

        # Ensure pipette stays within the working envelope
        pipette_position = np.clip(pipette_position, self.observation_space.low[:3], self.observation_space.high[:3])
        observation = np.concatenate((pipette_position, self.goal_position)).astype(np.float32)

        # Calculate the reward
        distance = np.linalg.norm(pipette_position - self.goal_position)
        reward = -self.reward_distance_scale * distance + self.step_penalty

        # Add bonus reward for success
        terminated = bool(distance < self.threshold)
        if terminated:
            reward += self.bonus_reward

        truncated = bool(self.steps >= self.max_steps)
        info = {"success": terminated}

        self.steps += 1

        return observation, reward, terminated, truncated, info  

    def render(self, mode='human'):
        pass
    
    def close(self):
        self.sim.close()
