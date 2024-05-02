import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from .graph_optimizer import GraphOptimizer
from config.settings import config
import matplotlib.animation as animation
import json
import os

data_path = os.path.join(os.getcwd(), 'data')

def load_data(year):
    filepath = f'data/{year}/graph_data.json'
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"No data found for the year {year}.")
        exit(1)

def plot_initial_optimized_positions(initial_positions, optimized_positions, edges):
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Set node colors, shapes, and labels
    initial_node_color = 'red'
    initial_node_shape = 'o'
    initial_label = 'Initial'
    optimized_node_color = 'lightblue'
    optimized_node_shape = 'o'
    optimized_label = 'Optimized'

    # Iterate over initial and optimized positions
    for ax_index, (positions, node_color, node_shape, label) in enumerate(zip([initial_positions, optimized_positions],
                                                                               [initial_node_color, optimized_node_color],
                                                                               [initial_node_shape, optimized_node_shape],
                                                                               [initial_label, optimized_label])):
        # Create a NetworkX graph
        G = nx.Graph()

        # Add nodes with positions
        for node, pos in positions.items():
            G.add_node(node, pos=pos)

        # Add edges
        G.add_edges_from(edges)

        # Draw nodes and edges
        nx.draw_networkx_nodes(G, pos=positions, ax=axes[ax_index], node_color=node_color, node_shape=node_shape, label=label, node_size=200)
        nx.draw_networkx_labels(G, pos=positions, ax=axes[ax_index], font_size=10, font_color='black', font_weight='bold')
        nx.draw_networkx_edges(G, pos=positions, ax=axes[ax_index], edge_color='gray')
        axes[ax_index].set_title(f"{label} - Year: {config.get('year', 'unknown year')}")

    # Display the plot
    plt.show()



def load_all_data():
    """
    Load graph data for all years in the data directory.
    Assumes graph_data.json exists for each year.
    """
    all_positions = {}
    all_distances = {}
    all_edge_lists = []

    for year_folder in os.listdir(data_path):
        year_path = os.path.join(data_path, year_folder)
        if os.path.isdir(year_path):
            with open(os.path.join(year_path, 'graph_data.json'), 'r') as f:
                data = json.load(f)
                positions = {
                    node: np.array(coords)
                    for node, coords in data['positions'].items()
                }
                distances = {
                    tuple(sorted((edge['from'], edge['to']))): edge['distance']
                    for edge in data['distances']
                }
                edge_list = list(distances.keys())

                all_positions[year_folder] = positions
                all_distances[year_folder] = distances
                all_edge_lists.append(edge_list)

    return all_positions, all_distances, all_edge_lists

def animate_yearly_optimizations(angle_weight):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title("Optimized Positions Over Years")
    G = nx.Graph()  # Initialize G outside the update function
    positions, distances, edge_lists = load_all_data()
    years = list(positions.keys())
    
    def update(frame, angle_weight = angle_weight):
        ax.clear()
        year = years[frame]
        year_positions = positions[year]
        year_distances = distances[year]
        year_edge_list = edge_lists[frame]
        
        # Clear and add edges and nodes to the graph
        G.clear()
        for edge, dist in year_distances.items():
            G.add_edge(*edge, weight=dist)
        for node, pos in year_positions.items():
            G.add_node(node)

        # Perform optimization
        optimizer = GraphOptimizer(year_positions, year_distances, angle_weight)
        optimized_positions = optimizer.optimize()

        # Draw the graph with optimized positions
        nx.draw(G, optimized_positions, ax=ax, with_labels=False, node_color='lightblue', node_size=150)
        nx.draw_networkx_labels(G, optimized_positions, ax = ax,  font_size=10, font_color='black', font_weight='bold')
        ax.set_title(f"Year: {year}")

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=len(years), repeat=True)
    plt.show()

def display_sorted_optimizations_by_weight(positions, distances):
    angle_weights = config['optimization_params']['angle_weights']
    results = []
    iteration_counts = []  # To store iteration counts for each weight

    for weight in angle_weights:
        optimizer = GraphOptimizer(positions, distances, weight)
        result = optimizer.optimize()
        results.append((weight, result))
        iteration_counts.append(len(optimizer.positions_history))  # Capture the number of iterations for each optimization

    num_weights = len(angle_weights)
    grid_size = int(np.ceil(np.sqrt(num_weights)))  # Compute grid dimensions
    fig, axes = plt.subplots(grid_size, grid_size, figsize=(grid_size * 5, grid_size * 5), subplot_kw={'xticks': [], 'yticks': []})  # Increase figure size for better spacing
    axes = axes.flatten()

    for idx, ((weight, pos), iterations) in enumerate(zip(results, iteration_counts)):
        ax = axes[idx]
        G = nx.Graph()
        G.add_nodes_from(positions.keys())
        G.add_edges_from(distances.keys())
        nx.draw(G, pos, ax=ax, with_labels=False, node_color='lightblue', node_size=150)
        nx.draw_networkx_labels(G, pos, ax = ax,  font_size=10, font_color='black', font_weight='bold')
        ax.set_title(f"Weight: {weight} - Iterations: {iterations}", fontsize=10)  # Smaller font size

    # Turn off axes for unused subplots if any
    for i in range(len(results), len(axes)):
        axes[i].axis('off')

    
    plt.tight_layout(pad=3.0)  # Increased padding for better margins
    plt.show()


def animate_iterations(positions_history, positions, distances):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title('Graph Layout Optimization')
    year = config.get("year","unknownyear")

    def animate(frame):
        ax.clear()
        pos = positions_history[frame]
        G = nx.Graph()
        G.add_nodes_from(positions.keys())
        G.add_edges_from(distances.keys())
        nx.draw(G, pos, ax=ax, with_labels=False, node_color='lightblue', node_size=250)
        nx.draw_networkx_labels(G, pos, ax = ax,  font_size=10, font_color='black', font_weight='bold')
        ax.set_title(f"year: {year} Iterations: {frame}", fontsize = 10)
        plt.pause(0.1 if frame > 0 else 5)  # Longer pause for the first frame

    ani = animation.FuncAnimation(fig, animate, frames=len(positions_history), repeat=True)
    plt.show()
    return


