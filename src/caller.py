import random

from dts.pbf import pbf_hg
from aux.plotter import visualization_caller, animation_caller
from aux.helper import *

random.seed(3)

inputs = dict(
    chamber_width=610,
    chamber_height=410,
    bed_height=300.,
    bed_is_leveled=True,
    bin_width=200.,
    blade_position=590.,
    blade_home_position=590.,
    blade_end_position=10.,
    blade_height=50.,
    blade_max_velocity=120.,
    hopper_x_position=400,
    hopper_initial_y_position=-140,
    hopper_raising_distance=1.5,
    hopper_width=200,
    hopper_is_raised=False,
    plate_x_position=200,
    height_tol=0.01,
    plate_width=200,
    plate_lowering_distance=-1,
    timestep=4.,
    time=0.0,
    laser_is_on=True,
    layer_scan_times=[8. + 4 * random.random() for i in range(30)],
    layers_completed=0,
    layer_start_time=0.0,
    prev_layer_fused=True,
)

debug_nodes = [
    'blade_is_clearing',
]
debug_edges = [
    'get_layers_completed',
]

t = pbf_hg.solve(
    'layer_just_fused',
    inputs,
    min_index=8,
    memory_mode=True,
    search_depth=2000,
    # to_print=True,
    # debug_nodes=debug_nodes,
    # debug_edges=debug_edges,
    # logging_level=10,
)

print_vals(t, 'time')
print_vals(t, 'layer_start_time')
print(f'scan times: {t.values['layer_scan_times'][0][:1]}')
print_vals(t, 'layer_fused')
print_vals(t, 'layers_completed')
print_vals(t, 'blade_is_clearing')
print_vals(t, 'bed_is_leveled')
print_vals(t, 'blade_position')
print_vals(t, 'blade_velocity')


# animation_caller(pbf_hg, inputs)

# visualization_caller(pbf_hg)
