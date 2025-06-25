from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from src.relations.relations import *

hopper_hg = Hypergraph()

# Nodes
hopper_x_position = Node(
    label='hopper_x_position',
    description='distance from left of chamber for hopper',
    units='mm',
)
hopper_y_position = Node(
    label='hopper_y_position',
    description='distance from bottom of chamber for hopper',
    units='mm',
)
hopper_width = Node(
    label='hopper_width',
    description='width of hopper',
    units='mm',
)
