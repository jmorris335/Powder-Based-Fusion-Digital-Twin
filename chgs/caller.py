import random

from dts.pbf import pbf_hg
from aux.plotter import visualization_caller, animation_caller
from aux.helper import *

random.seed(3)

inputs = dict(
    bed_height=300.,
    bed_is_leveled=True,
    bin_width=200.,
    blade_position=590.,
    blade_home_position=590.,
    blade_end_position=10.,
    blade_height=50.,
    blade_max_velocity=350.,
    blade_is_leveling=False,
    blade_is_returning=False,
    blade_is_clearing=False,
    chamber_width=610,
    chamber_height=410,
    height_tol=0.01,
    hopper_x_position=400,
    hopper_initial_y_position=-140,
    hopper_raising_distance=1.5,
    hopper_width=200,
    laser_is_on=True,
    layer_scan_times=[2. + 1 * random.random() for i in range(30)],
    layers_completed=0,
    material_density=0.0027,
    scan_start_time=0.0,
    plate_x_position=200,
    plate_width=200,
    plate_lowering_distance=-1,
    prev_layer_fused=True,
    timestep=0.5,
    time=0.0,
)

debug_nodes = [
    'blade_is_clearing',
]
debug_edges = [
    'layer_finished_scanning',
]

t = pbf_hg.solve(
    'blade_position',
    inputs,
    min_index=3,
    # search_depth=500,
    to_print=True,
    # debug_nodes=debug_nodes,
    # debug_edges=debug_edges,
    # logging_level=10,
)
print(t if t is not None else "No solutions")

# print_vals(t, 'time')
# print_vals(t, 'bed_is_leveled')
# print_vals(t, 'scan_start_time')
# print_vals(t, 'scan_end_time')
# print_vals(t, 'layer_just_fused')
# print_vals(t, 'layer_fused')
# print_vals(t, 'layers_completed')
# print_vals(t, 'blade_is_leveling')
# print_vals(t, 'blade_is_clearing')
# print_vals(t, 'blade_is_returning')
# print_vals(t, 'blade_velocity')
# print_vals(t, 'blade_position')
# print_vals(t, 'blade_relative_position')        


# visualization_caller(pbf_hg)

animation_caller(pbf_hg, inputs, frames=101)