
import matplotlib.pyplot as plt
import networkx as nx
from src.graph_optimizer import GraphOptimizer
from src.utilities import (plot_initial_optimized_positions, animate_yearly_optimizations,
                       display_sorted_optimizations_by_weight, animate_iterations, load_data)
from config.settings import config
import numpy as np



def main():
    # import parameters from config
    year = config.get('year')
    data = load_data(year)
    positions = {
        node: np.array(coords)
        for node, coords in data['positions'].items()
        }
    
    distances = {
    tuple(sorted((edge['from'], edge['to']))): edge['distance']
    for edge in data['distances']
    }

    edge_list = list(distances.keys())

    angle_weight = config["optimization_params"]['angle_weight']
    
    #print(positions)
    #print(distances)
    optimizer = GraphOptimizer(positions, distances, angle_weight)
    optimized_positions = optimizer.optimize()  # Run optimization once and reuse the result

    if config['plot_initial_vs_optimized']:
        plot_initial_optimized_positions(positions,optimized_positions, edge_list)

    if config['animate_yearly_optimizations']:
        animate_yearly_optimizations(angle_weight)
    
    if config['display_sorted_by_the_weight_of_angle']:
        display_sorted_optimizations_by_weight(positions, distances)

    if config['animate_iterations']:
        animate_iterations(optimizer.positions_history, positions, distances)

if __name__ == '__main__':
    main()
