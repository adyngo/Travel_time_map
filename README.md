
# Visualization for Travel Time Map

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
In the `settings.py` file located in the `config` directory, you can adjust various parameters that affect the visualization and processing of the travel times. Also, you can activate various functions by setting their corresponding values to True. You can add new travel time data to the `data` directory. Ensure the new data follows the JSON format as shown in existing files.

## Usage
To run the project, execute the following command in the terminal:
```bash
python main.py
```
This will initiate the script to process the data and display the travel time maps.



## Data Description
The data in the `data/2000` and `data/2024` directories represent train travel time data in Hokkaido. This data is used to plot locations and optimize the 2D graph to visually represent travel times. Each data file should contain positions and distances structured similarly to the provided JSON format.

## Features and Functionalities
- `plot_initial_optimized_positions`: Plots the initial positions based on provided data.
- `animate_yearly_optimizations`: Creates an animation showing yearly changes in optimizations.
- `display_sorted_optimizations_by_weight`: Displays optimized graphs sorted by their weight.
- `animate_iterations`: Generates animations showing the iterative process of optimizations.

