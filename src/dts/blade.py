from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from src.relations.relations import *

blade_hg = Hypergraph()

# Nodes
timestep = Node('timestep', description='smallest time unit considered', units='s')
blade_name = Node('blade_name', description='name for blade')
blade_type = Node('blade_type', description='type of blade')
blade_angle = Node('blade_angle', description='angle for blade', units='degrees')
blade_position = Node(
    label='blade_position',
    description='distance of blade from start position',
    units='mm',
)
blade_velocity = Node(
    label='blade_velocity',
    description='velocity of blade, with + moving away from start position',
    units='mm/s',
)
blade_is_clearing = Node(
    label='blade_is_clearing',
    description='true if blade is clearing bed',
    units='Boolean',
)
blade_is_returning = Node(
    label='blade_is_returning',
    description='true if blade is returning to start position',
    units='Boolean',
)

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