# Visualization for Travel Time Map

*"This is the repository for the 2024 project assignment in Remote Sensing and Geographic Information Systems."*

## Project Description
**Visualization for Travel Time Map** is a Python project designed to visualize travel times by representing them as the lengths of edges between points on a 2D map. This project uses train travel time data from Hokkaido to create an optimized graphical representation of travel routes and durations.

## Installation Instructions
### Prerequisites
- Python 3.10 or later
- Libraries: matplotlib, networkx, numpy, scipy

### Setup
1. Clone the repository to your local machine.
2. Install the required Python libraries using pip:
   ```bash
   pip install matplotlib networkx numpy scipy
   ```
3. Navigate to the project directory.

## Settings
In the `settings.py` file located in the `config` directory, you can adjust various parameters that affect the visualization and processing of the travel times. Also, you can activate various functions by setting their corresponding values to True.

```Python
config = {
    'year': 2024, #year to use in "plot_initial_optimized_positions", "display_sorted_optimizations_by_weight", and "animate_iterations"
    'plot_initial_vs_optimized': True,  #You can use these functions by setting this "True"
    'animate_yearly_optimizations': True,
    'display_sorted_by_the_weight_of_angle': False,
    'animate_iterations': True,

    # Parameters specific to graph optimization
    'optimization_params': {
        'angle_weight': 0.5, #Angle weight to use in "plot_initial_optimized_positions", "animate_yearly_optimizations", and "animate_iterations"
        'angle_weights': [0,0.1, 0.5, 1.0,10,100,1000], # Different angle weights to use in "display_sorted_optimizations_by_weight"
        'animation_interval': 50,          # Interval for animation frames in milliseconds
    }
}
```

 You can add new travel time data to the `data` directory. Ensure the new data follows the JSON format as shown in existing files.

## Usage
To run the project, execute the following command in the terminal:
```bash
python main.py
```
This will initiate the script to process the data and display the travel time maps.

## Data Description
The data in the `data/1980`, `data/2000`, and `data/2024` directories represent train travel time data in Hokkaido. This data is used to plot locations and optimize the 2D graph to visually represent travel times. Each data file should contain positions and distances structured similarly to the provided JSON format.  
Example
```json
{
    "positions": {
      "Sapporo": [0.0, 0.0],
      "Obihiro": [18.511, -1.506]
    },
      "distances": [
        {"from": "Sapporo", "to": "Chitose", "distance": 46.0},
        {"from": "Sapporo", "to": "Otaru", "distance": 39.0}
      ]
    }    
```
## Features and Functionalities
- `plot_initial_optimized_positions`: Plots the initial and optimized positions based on provided data.  

- `display_sorted_optimizations_by_weight`: Displays optimized graphs sorted by their weight.  

- `animate_yearly_optimizations`: Creates an animation showing yearly changes in optimizations.  

- `animate_iterations`: Generates animations showing the iterative process of optimizations.  
