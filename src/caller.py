from dts.pbf import pbf_hg
from aux.plotter import visualization_caller

inputs = dict(
    chamber_width=6.1,
    chamber_height=4.1,
    bed_height=3.,
    bin_width=2.,
    blade_position=5.8,
    blade_height=0.5,
    hopper_x_position=4,
    hopper_y_position=1.4,
    hopper_width=2,
    build_plate_x_position=2,
    build_plate_y_position=2.1,
    build_plate_width=2,
)

pbf_hg.solve('blade_position', inputs)
visualization_caller(pbf_hg)


