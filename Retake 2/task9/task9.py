from sim_class import Simulation
import pybullet as p
import os
import json

# Initialize the simulation with a specified number of agents
sim = Simulation(num_agents=1)  # For one robot

# Create output directory
os.makedirs('output', exist_ok=True)
pipette_state_file = open('output/pipette_state.txt', 'a')
state_dict = {}

# Define the corner velocities for the working envelope
# Velocities are adjusted to move to min/max for X, Y, Z

corner_velocities = [
    [-0.7, -0.7, -0.7, 0],  # Bottom-front-left
    [0.7, -0.7, -0.7, 0],  # Bottom-front-right
    [0.7,  0.7, -0.7, 0],  # Bottom-back-right 
    [-0.7,  0.7, -0.7, 0],  # Bottom-back-left
    [-0.7,  0.7,  0.7, 0],  # Top-back-left
    [0.7,  0.7,  0.7, 0],  # Top-back-right
    [0.7, -0.7,  0.7, 0],  # Top-front-right
    [-0.7, -0.7,  0.7, 0],  # Top-front-left
]

for idx, velocities in enumerate(corner_velocities):
    actions = [[*velocities, 0]]  # 0 = no drop
    state = sim.run(actions, num_steps=200)
    agent_id = list(state.keys())[0]
    pipette_position = state[agent_id]["pipette_position"]

    # Print the position to console
    print(f"Corner {idx}: {pipette_position}")

# Save full state
with open('output/state.json', 'w') as f:
    json.dump(state_dict, f, indent=4)

pipette_state_file.close()