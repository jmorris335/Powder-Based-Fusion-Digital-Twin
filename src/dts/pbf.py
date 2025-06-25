from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from dts.chamber import chamber_hg
from dts.part import part_hg
from relations.relations import *

pbf_hg = Hypergraph()
pbf_hg.union(pbf_hg, chamber_hg, part_hg)

# Nodes
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
layers_completed = pbf_hg.add_node(Node(
    label='layers_completed',
    description='number of layers completed',
))
layer_start_time = pbf_hg.add_node(Node(
    label='layer_start_time',
    description='time current layer was first prepared for fusing',
    units='s',
))
scan_time = pbf_hg.add_node(Node(
    label='scan_time',
    description='time required to fuse current layer',
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
layer_complete = pbf_hg.add_node(Node(
    label='layer_complete',
    description='true if no more actions need to occur on current layer',
    units='Boolean',
))
amount_in_stock = pbf_hg.add_node(Node(
    label='amount_in_stock',
    description='amount of material remaining in stock',
    units='g',
))
current_material = pbf_hg.add_node(Node(
    label='current_material',
    description='name of material currently loaded in chamber',
))

# Edges
pbf_hg.add_edge(
    {'scan_time': scan_time,
     'keyframe': layer_start_time,
     'time': time},
    target=layer_fused,
    rel=Rlayer_finished_scanning,
    edge_props=['LEVEL', 'DISPOSE_ALL'],
)
pbf_hg.add_edge(
    {'fused': layer_fused,
     'complete': layer_complete},
    target=laser_is_on,
    rel=R.Rnot_any
)
pbf_hg.add_edge(
    {'time': time,
     'step': timestep},
    target=time,
    rel=R.Rsum,
    index_offset=1,
    disposable=['time'],
)