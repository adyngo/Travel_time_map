# Configuration settings for the Graph Layout Optimization Project
# You can chance parameters of the functions and data by editing them here.

config = {
    'year': 2024, #year to use in "plot_initial_optimized_positions", "display_sorted_optimizations_by_weight", and "animate_iterations"

    'plot_initial_vs_optimized': True,  #You can use these function by setting this "True"
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
