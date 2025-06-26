import random

from dts.pbf import pbf_hg
from aux.plotter import visualization_caller

inputs = dict(
    chamber_width=610,
    chamber_height=410,
    bed_height=300.,
    bin_width=200.,
    blade_position=580,
    blade_height=50,
    hopper_x_position=400,
    hopper_y_position=140,
    hopper_width=200,
    build_plate_x_position=200,
    build_plate_y_position=210,
    build_plate_width=200,
    plate_lowering_distance=-1,
    hopper_raising_distance=1.5,
    timestep=0.5,
    time=63.71,
    laser_is_on=True,
    layer_build_times = [8. + 4 * random.random() for i in range(30)],
)

t = pbf_hg.solve('build_progress', inputs, memory_mode=True)
print(t)
visualization_caller(pbf_hg)


