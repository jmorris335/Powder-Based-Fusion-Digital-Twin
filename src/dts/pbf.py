from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from dts.chamber import chamber_hg
from dts.part import part_hg

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
scan_time = pbf_hg.add_node(Node(
    label='scan_time',
    description='time required to fuse current layer',
    units='s',
))
layer_complete = pbf_hg.add_node(Node(
    label='layer_complete',
    description='true if current layer has been completely fused',
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

# Relations
