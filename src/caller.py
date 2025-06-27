import random

from dts.pbf import pbf_hg
from aux.plotter import visualization_caller, animation_caller

inputs = dict(
    chamber_width=610,
    chamber_height=410,
    bed_height=300.,
    bed_is_leveled=True,
    bin_width=200.,
    blade_position=600.,
    blade_home_position=600.,
    blade_end_position=10.,
    blade_height=50.,
    blade_max_velocity=120.,
    hopper_x_position=400,
    hopper_initial_y_position=-140,
    hopper_raising_distance=1.5,
    hopper_width=200,
    hopper_is_raised=False,
    plate_x_position=200,
    plate_initial_y_position=300,
    plate_width=200,
    plate_lowering_distance=-1,
    timestep=2,
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
    'check_blade_is_clearing',
]

t = pbf_hg.solve(
    'bed_is_leveled',
    inputs,
    min_index=4,
    memory_mode=True,
    # to_print=True,
    # debug_nodes=debug_nodes,
    # debug_edges=debug_edges,
    # logging_level=10,
)
print(t.print_tree())
print(t.values['build_progress'])
#ff0000: For some reason found values of build progress past index 1 aren't being collected in t.values

# animation_caller(pbf_hg, inputs)

# visualization_caller(pbf_hg)
