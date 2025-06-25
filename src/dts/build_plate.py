from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from src.relations.relations import *

plate_hg = Hypergraph()

# Nodes
build_plate_x_position = Node(
    label='build_plate_x_position',
    description='distance from left of chamber for build plate',
    units='mm',
)
build_plate_y_position = Node(
    label='build_plate_y_position',
    description='distance from bottom of chamber for build plate',
    units='mm',
)
build_plate_width = Node(
    label='build_plate_width',
    description='width of build plate',
    units='mm',
)