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
hopper_depth = hopper_hg.add_node(Node(
    label='hopper_depth',
    description='depth of hopper',
    units='mm',
))
hopper_volume = hopper_hg.add_node(Node(
    label='hopper_volume',
    description='volume of hopper',
    units='mm^3',
))

##    Material    ######################################################
current_material = hopper_hg.add_node(Node(
    label='current_material',
    description='name of material currently loaded in chamber',
))
material_density = hopper_hg.add_node(Node(
    label='current_material',
    description='average density of material',
    units='g/mm^3',
))
material_mass = hopper_hg.add_node(Node(
    label='material_mass',
    description='mass of material in hopper',
    units='g',
))


########################################################################
##    Edges
########################################################################


hopper_hg.add_edge(
    sources=hopper_width,
    target=hopper_depth,
    rel=R.Rfirst,
)
hopper_hg.add_edge(
    sources=[hopper_width, hopper_depth, hopper_y_position],
    target=hopper_volume,
    rel=R.Rmultiply,
)
hopper_hg.add_edge(
    {'density': material_density,
     'volume': hopper_volume},
    target=material_mass,
    rel=R.Rmultiply
)
