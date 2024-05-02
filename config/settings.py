# Configuration settings for the Graph Layout Optimization Project

# General application settings
config = {
    'year': 2000,
    'plot_initial_vs_optimized': False,
    'animate_yearly_optimizations': False,
    'display_sorted_by_the_weight_of_angle': True,
    'animate_iterations': True,

    # Parameters specific to graph optimization
    'optimization_params': {
        'angle_weight': 0.1,
        'angle_weights': [0,0.1, 0.5, 1.0,10,100,1000], # Different angle weights to use in optimization
        'animation_interval': 50,          # Interval for animation frames in milliseconds
    }
}
