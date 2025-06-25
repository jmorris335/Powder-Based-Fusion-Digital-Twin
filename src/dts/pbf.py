from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from dts.blade import blade_hg
from dts.build_plate import plate_hg
from dts.chamber import chamber_hg
from dts.hopper import hopper_hg

pbf_hg = Hypergraph()
pbf_hg.union(pbf_hg, blade_hg, plate_hg, chamber_hg, hopper_hg)

# Nodes
build_time = pbf_hg.add_node(Node(
    label='build_time',
    description='time to build part',
    units='s',
))
build_progress = pbf_hg.add_node(Node(
    label='build_progress',
    description='proportion of build completed',
    units='%',
))
layers_completed = pbf_hg.add_node(Node(
    label='layers_completed',
    description='number of layers completed',
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