from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

plate_hg = Hypergraph()

# Nodes
plate_x_position = plate_hg.add_node(Node(
    label='build_plate_x_position',
    description='distance from left of chamber for build plate',
    units='mm',
))
plate_y_position = plate_hg.add_node(Node(
    label='build_plate_y_position',
    description='distance from bottom of chamber for build plate',
    units='mm',
))
plate_width = plate_hg.add_node(Node(
    label='build_plate_width',
    description='width of build plate',
    units='mm',
))