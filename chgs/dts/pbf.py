from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from dts.chamber import chamber_hg
from dts.part import part_hg
from relations.relations import *

pbf_hg = chamber_hg + part_hg


########################################################################
##    Nodes
########################################################################


##    Time    ##########################################################
timestep = pbf_hg.add_node(Node(
    label='timestep',
    description='smallest time unit considered',
    units='s',
))
time = pbf_hg.add_node(Node(
    label='time',
    description='current time of process',
    units='s',
))
build_time = pbf_hg.add_node(Node(
    label='build_time',
    description='time to build part',
    units='s',
))

##    Layers    ########################################################
layer_thickness = pbf_hg.add_node(Node(
    label='layer_thickness',
    description='height of each layer of the part',
    units='mm'
))
layers_completed = pbf_hg.add_node(Node(
    label='layers_completed',
    description='number of layers completed',
))
build_progress = part_hg.add_node(Node(
    label='build_progress',
    description='proportion of build completed',
    units='%',
))
layer_scan_times = part_hg.add_node(Node(
    label='layer_scan_times',
    description='list of times to build each layer',
    units='List[s]',
))
layer_scan_time = pbf_hg.add_node(Node(
    label='layer_scan_time',
    description='time required to fuse current layer',
    units='s',
))

##    Laser    #########################################################
scan_start_time = pbf_hg.add_node(Node(
    label='scan_start_time',
    description='time current layer was first prepared for fusing',
    units='s',
))
scan_end_time = pbf_hg.add_node(Node(
    label='scan_end_time',
    description='time fusing should end for current layer',
    units='s',
))
laser_is_on = pbf_hg.add_node(Node(
    label='laser_is_on',
    description='true if laser is on',
    units='Boolean',
))
layer_fused = pbf_hg.add_node(Node(
    label='layer_fused',
    description='true if current layer has been completely fused',
    units='Boolean',
))
layer_just_fused = pbf_hg.add_node(Node(
    label='layer_just_fused',
    description='true if current layer was been fused on the current index',
    units='Boolean',
))

##    Bed    ###########################################################
bed_height = pbf_hg.add_node(Node(
    label='bed_height',
    description='distance of bed surface from floor',
    units='mm',
))
bed_is_leveled = pbf_hg.add_node(Node(
    label='bed_is_leveled',
    description='true if bed is ready for fusion to begin',
    units='Boolean',
))
height_tol = pbf_hg.add_node(Node(
    label='height_tol',
    description='tolerance for machine adjustments in height',
    units='mm',
))

##    Build Plate    ###################################################
plate_y_position = pbf_hg.add_node(Node(
    label='plate_y_position',
    description='distance from bottom of chamber to build plate',
    units='mm',
))
plate_initial_y_position = pbf_hg.add_node(Node(
    label='plate_initial_y_position',
    description='initial distance from bottom of chamber to build plate',
    units='mm',
))
plate_lowering_distance = pbf_hg.add_node(Node(
    label='plate_lowering_distance',
    description='distance plate lowers after fusion process',
    units='mm'
))
plate_at_fusion_level = pbf_hg.add_node(Node(
    label='plate_at_fusion_level',
    description='true if plate is high enough for fusion/leveling process',
    units='Boolean',
))

##    Hopper    ########################################################
hopper_initial_y_position = pbf_hg.add_node(Node(
    label='hopper_initial_y_position',
    description='initial distance from hopper floor to build plate',
    units='mm',
))
hopper_y_position = pbf_hg.add_node(Node(
    label='hopper_y_position',
    description='distance from bed surface to hopper floor (usually negative)',
    units='mm',
))
hopper_raising_distance = pbf_hg.add_node(Node(
    label='hopper_raising_distance',
    description='distance plate raises after fusion process',
    units='mm'
))
hopper_is_raised = pbf_hg.add_node(Node(
    label='hopper_is_raised',
    description='true if hopper is one level above current layer',
    units='Boolean',
))

##    Blade    #########################################################
leveling_time = pbf_hg.add_node(Node(
    label='leveling_time',
    description='Nominal duration of leveling process',
    units='s',
))
blade_is_leveling = pbf_hg.add_node(Node(
    label='blade_is_leveling',
    description='true if the blade is currently moving',
    units='Boolean',
))
blade_is_clearing = pbf_hg.add_node(Node(
    label='blade_is_clearing',
    description='true if blade is actively clearing bed',
    units='Boolean',
))
blade_returned = pbf_hg.add_node(Node(
    label='blade_returned',
    description='true if blade is in its home position',
    units='Boolean',
))
blade_at_end = pbf_hg.add_node(Node(
    label='blade_at_end',
    description='true if blade is in its end position',
    units='Boolean',
))
blade_is_returning = pbf_hg.add_node(Node(
    label='blade_is_returning',
    description='true if blade returning to its home position',
    units='Boolean',
))
blade_position = pbf_hg.add_node(Node(
    label='blade_position',
    description='distance of blade from left of chamber',
    units='mm',
))
blade_relative_position = pbf_hg.add_node(Node(
    label='blade_relative_position',
    description='proportion of blade location from home (0) to end (1) position',
))
blade_home_position = pbf_hg.add_node(Node(
    label='blade_home_position',
    description='home position for blade from left of chamber',
    units='mm',
))
blade_end_position = pbf_hg.add_node(Node(
    label='blade_end_position',
    description='maximum position for blade from left of chamber',
    units='mm',
))


########################################################################
##    Edges
########################################################################


##    Time    ##########################################################
pbf_hg.add_edge(
    {'time': time,
     'step': timestep},
    target=time,
    rel=R.Rsum,
    index_offset=1,
    disposable=['time'],
)
pbf_hg.add_edge(
    {'index': layers_completed,
     'times': layer_scan_times},
    target=layer_scan_time,
    rel=lambda index, times, **kw : times[index],
    via=lambda times, index, **kw : index < len(times),
    disposable='index',
)
pbf_hg.add_edge(
    {'scan_times': layer_scan_times,
     'leveling_time': leveling_time},
    target=build_time,
    rel=Rcalc_build_time,
)

##    Build Process    #################################################
pbf_hg.add_edge(
    {'leveled': bed_is_leveled,
     'progress': build_progress,
     'time': time,
     'prev_start': scan_start_time},
    target=scan_start_time,
    rel=Rcalc_fusing_start_time,
    index_offset=1,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'scan_time': layer_scan_time,
    'time':time},
    target=scan_end_time,
    rel=R.Rsum,
    index_via=lambda scan_time, time, **kw : time == 1 and scan_time == 1,
    edge_props=['DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'leveled': bed_is_leveled,
     'scan_time': layer_scan_time,
     'start': scan_start_time,
     'prev': scan_end_time},
    target=scan_end_time,
    rel=Rcalc_fusing_end_time,
    index_offset=1,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'scan_end_time': scan_end_time,
     'time': time},
    target=layer_fused,
    rel=Rlayer_finished_scanning,
    label='layer_finished_scanning',
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'step': timestep,
     'time': time,
     'keyframe': scan_end_time},
    target=layer_just_fused,
    rel=Rcheck_event_just_happened,
    index_via=lambda time, keyframe, **kw : R.Rsame(time, keyframe),
    disposable=['time', 'keyframe'],
)
pbf_hg.add_edge(
    {'just_fused': layer_just_fused,
     'prev_layers': layers_completed},
    target=layers_completed,
    label='get_layers_completed',
    rel=Rget_layers_completed,
    index_offset=1,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'keyframe': scan_start_time,
     'time': time,
     'finished': layer_fused},
    target=laser_is_on,
    label='check_laser_on',
    rel=Rcheck_laser_on,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'height': plate_y_position,
     'initial': bed_height, #Should this be plate_initial_y_position
     'num_layers': layers_completed,
     'step': plate_lowering_distance,
     'tol': height_tol},
    target=plate_at_fusion_level,
    rel=Rcheck_plate_at_fusion_level,
    index_via=lambda height, num_layers, **kw : R.Rsame(height, num_layers),
    disposable=['height', 'num_layers'],
)
"""This is a good example of an assumption violated by a scope change.
This edge assumes that there is a constant hopper_raising_distance for 
each level of the print. If that assumption was violated (by some smart 
adjustment algorithm perhaps), then the edge would not be able to handle
the input data of multiple hopper_raising_distances, and would cease to 
be valid.
"""
pbf_hg.add_edge(
    {'height': hopper_y_position,
     'initial': hopper_initial_y_position,
     'num_layers': layers_completed,
     'step': hopper_raising_distance,
     'tol': height_tol},
    target=hopper_is_raised,
    rel=Rcheck_hopper_at_leveling_level,
    index_via=lambda height, num_layers, **kw : R.Rsame(height, num_layers),
    disposable=['height', 'num_layers'],
)
pbf_hg.add_edge(
    {'start': bed_height,
     'step': plate_lowering_distance},
    target=plate_initial_y_position,
    rel=R.Rsum,
)
pbf_hg.add_edge(
    {'step': plate_lowering_distance,
     'count': layers_completed,
     'start': plate_initial_y_position},
    target=plate_y_position,
    rel=Rcalc_vertical_position,
    disposable='layers_completed',
)
pbf_hg.add_edge(
    {'step': hopper_raising_distance,
     'count': layers_completed,
     'start': hopper_initial_y_position},
    target=hopper_y_position,
    rel=Rcalc_vertical_position,
    disposable='layers_completed',
)
pbf_hg.add_edge(
    {'fused': layer_fused,
     'plate': plate_at_fusion_level,
     'hopper': hopper_is_raised,
     'bed': bed_is_leveled},
    target=blade_is_leveling,
    label='check_blade_is_leveling',
    rel=Rcheck_blade_is_leveling,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'prev': bed_is_leveled,
     'firing': laser_is_on,
     'returning': blade_is_returning,
     'rel_pos': blade_relative_position},
    target=bed_is_leveled,
    label='check_bed_leveled',
    rel=Rcheck_bed_leveled,
    index_offset=1,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)