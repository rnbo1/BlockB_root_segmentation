# Simulation Environment

This markdown file provides instructions on how to set the simulation environment, including list of dependancies, and details about the working envelope of the pipette.

## Environment set up

1. **Python Version**
    
    Ensure you have Python 3.7 or later installed.

2. **Install Dependecies**
   
    Install the required library using `pip`:

    pip install pybullet

3. Clone the Simulation Repository
 
    git clone https://github.com/BredaUniversityADSAI/Y2B-2023-OT2_Twin.git
    cd Y2B-2023-OT2_Twin

4. Run the Simulation

    Execute the provided Python script:

        python simulation.py

## Dependecies

The simulation requires:

    `pybullet`: Physics simulation and rendering engine.

Install with:

    pip install pybullet

## Working Envelope of the Pipette
To determine the working envelope, the pipette was moved to each of the 8 corners of a 3D cube using velocity vectors. The pipette tip positions were recorded at each location

### Corner Points of the Envelope

| Corner | Name               | X        | Y        | Z        |
|--------|--------------------|----------|----------|----------|
| 0      | Bottom-front-left  | -0.187   | -0.1707  | 0.1196   |
| 1      | Bottom-front-right | 0.253    | -0.1707  | 0.1199   |
| 2      | Bottom-back-right  | 0.253    | 0.2195   | 0.1203   |
| 3      | Bottom-back-left   | -0.187   | 0.2195   | 0.1205   |
| 4      | Top-back-left      | -0.187   | 0.2195   | 0.2895   |
| 5      | Top-back-right     | 0.2531   | 0.2201   | 0.2898   |
| 6      | Top-front-right    | 0.2532   | -0.1705  | 0.2895   |
| 7      | Top-front-left     | -0.187   | -0.1705  | 0.2895   |

These were printed to the console and saved in:
- `output/pipette_state.txt` - readable text log
- `output/state.json` - full state data

## Running the Simulation

To simulate the movement:
- The robot is initialised and commanded using velocity vectors.
- The pipette is moved in 3D space toward each envelope corner.
- Obdervations are collected and saved.

Refer to `simulation.py` for the full script. 


## Notes

- If errors are encountered, ensure `PyBullet` is installed and correctly configured.
- The simulation resets the robot between movements for consistent result.