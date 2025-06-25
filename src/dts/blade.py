from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

blade_hg = Hypergraph()

# Nodes
timestep = blade_hg.add_node(Node(
    label='timestep',
    description='smallest time unit considered',
    units='s',
))
blade_name = blade_hg.add_node(Node(
    label='blade_name',
    description='name for blade'
))
blade_type = blade_hg.add_node(Node(
    label='blade_type',
    description='type of blade'
))
blade_angle = blade_hg.add_node(Node(
    label='blade_angle',
    description='angle for blade',
    units='degrees',
))
blade_height = blade_hg.add_node(Node(
    label='blade_height',
    description='height of blade',
    units='mm',
))
blade_position = blade_hg.add_node(Node(
    label='blade_position',
    description='distance of blade from start position',
    units='mm',
))
blade_velocity = blade_hg.add_node(Node(
    label='blade_velocity',
    description='velocity of blade, with + moving away from start position',
    units='mm/s',
))
blade_is_clearing = blade_hg.add_node(Node(
    label='blade_is_clearing',
    description='true if blade is clearing bed',
    units='Boolean',
))
blade_is_returning = blade_hg.add_node(Node(
    label='blade_is_returning',
    description='true if blade is returning to start position',
    units='Boolean',
))

# Relations
blade_hg.add_edge(
    blade_velocity,
    target=blade_is_clearing,
    rel=Ris_positive,
)
blade_hg.add_edge(
    blade_velocity,
    target=blade_is_returning,
    rel=Ris_negative,
)