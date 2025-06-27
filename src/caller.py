import random

from dts.pbf import pbf_hg
from aux.plotter import visualization_caller

inputs = dict(
    chamber_width=610,
    chamber_height=410,
    bed_height=300.,
    bin_width=200.,
    blade_position=600.,
    blade_home_position=600.,
    blade_end_position=10.,
    blade_height=50,
    hopper_x_position=400,
    hopper_initial_y_position=-140,
    hopper_raising_distance=1.5,
    hopper_width=200,
    plate_x_position=200,
    plate_initial_y_position=210,
    plate_width=200,
    plate_lowering_distance=-1,
    timestep=1,
    time=0.0,
    laser_is_on=True,
    layer_scan_times=[8. + 4 * random.random() for i in range(30)],
    layers_completed=0,
)

t = pbf_hg.solve(
    'layers_completed',
    inputs,
    min_index=0,
    search_depth=150,
    memory_mode=True,
)
print(t)
# visualization_caller(pbf_hg)
