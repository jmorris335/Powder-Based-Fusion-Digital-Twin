from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

hopper_hg = Hypergraph()

# Nodes
hopper_x_position = hopper_hg.add_node(Node(
    label='hopper_x_position',
    description='distance from left of chamber for hopper',
    units='mm',
))
hopper_y_position = hopper_hg.add_node(Node(
    label='hopper_y_position',
    description='distance from bottom of chamber for hopper',
    units='mm',
))
hopper_width = hopper_hg.add_node(Node(
    label='hopper_width',
    description='width of hopper',
    units='mm',
))
