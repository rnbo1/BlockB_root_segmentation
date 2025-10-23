from ot2_gym_wrapper import OT2Env
import numpy as np

# Create the environment
env = OT2Env(render=False)

# Reset it
obs, info = env.reset()
print("Initial observation:", obs)

# Run 1000 random steps
for step in range(1000):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Step {step}: Reward={reward}, Terminated={terminated}, Truncated={truncated}")
    if terminated or truncated:
        break

# Close the environment
env.close()