import numpy as np
from scipy.optimize import minimize
from config.settings import config

class GraphOptimizer:
    def __init__(self, positions, distances, weight):
        self.positions = positions
        self.distances = distances
        self.initial_pos = np.concatenate([positions[n] for n in positions]).flatten()
        self.positions_history = [positions.copy()]
        self.initial_angles = {
            edge: np.arctan2(positions[edge[1]][1] - positions[edge[0]][1], positions[edge[1]][0] - positions[edge[0]][0])
            for edge in distances
            }
        self.weight = weight

    def cost_function(self, pos):
        pos_dict = {node: pos[2*i:2*i+2] for i, node in enumerate(self.positions)}
        cost = 0
        for edge, target_dist in self.distances.items():
            u, v = edge
            calculated_dist = np.linalg.norm(pos_dict[u] - pos_dict[v])
            cost += (calculated_dist - target_dist) ** 2
        
            current_angle = np.arctan2(pos_dict[v][1] - pos_dict[u][1], pos_dict[v][0] - pos_dict[u][0])
            angle_diff = np.fmod(current_angle - self.initial_angles[edge] + np.pi, 2 * np.pi) - np.pi
            cost += (angle_diff ** 2) * self.weight  # 角度誤差の重み
        return cost

    def optimize(self):
        result = minimize(self.cost_function, self.initial_pos, method='BFGS', callback=self.callback)
        optimized_positions = {n: result.x[2*i:2*i+2] for i, n in enumerate(self.positions)}
        return optimized_positions

    def callback(self, xk):
        # Update the positions history after each iteration
        updated_positions = {node: xk[2*i:2*i+2] for i, node in enumerate(self.positions)}
        self.positions_history.append(updated_positions)
