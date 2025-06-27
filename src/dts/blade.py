from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

blade_hg = Hypergraph()

########################################################################
##    Nodes
########################################################################


timestep = blade_hg.add_node(Node(
    label='timestep',
    description='smallest time unit considered',
    units='s',
))
leveling_time = blade_hg.add_node(Node(
    label='leveling_time',
    description='Nominal duration of leveling process',
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
blade_home_position = blade_hg.add_node(Node(
    label='blade_home_position',
    description='home position for blade from left of chamber',
    units='mm',
))
blade_end_position = blade_hg.add_node(Node(
    label='blade_end_position',
    description='maximum position for blade from left of chamber',
    units='mm',
))
blade_position = blade_hg.add_node(Node(
    label='blade_position',
    description='distance of blade from start position',
    units='mm',
))
blade_relative_position = blade_hg.add_node(Node(
    label='blade_relative_position',
    description='proportion of blade location from home (0) to end (1) position',
))
blade_velocity = blade_hg.add_node(Node(
    label='blade_velocity',
    description='current velocity of blade, with + moving away from start position',
    units='mm/s',
))
blade_max_velocity = blade_hg.add_node(Node(
    label='blade_max_velocity',
    description='goal velocity of blade, with + moving away from start position',
    units='mm/s',
))
blade_is_leveling = blade_hg.add_node(Node(
    label='blade_is_leveling',
    description='true if blade is leveling bed',
    units='Boolean',
))
blade_is_clearing = blade_hg.add_node(Node(
    label='blade_is_clearing',
    description='true if blade is clearing bed',
    units='Boolean',
))
bed_is_level = blade_hg.add_node(Node(
    label='bed_is_level',
    description='true if bed is adequately cleared',
    units='Boolean',
))
blade_is_returning = blade_hg.add_node(Node(
    label='blade_is_returning',
    description='true if blade is returning to start position',
    units='Boolean',
))
blade_returned = blade_hg.add_node(Node(
    label='blade_returned',
    description='true if blade is in its home position',
    units='Boolean',
))
blade_at_end = blade_hg.add_node(Node(
    label='blade_at_end',
    description='true if blade is in its end position',
    units='Boolean',
))


########################################################################
##    Edges
########################################################################


blade_hg.add_edge(
    {'is_clearing': blade_is_clearing,
     'speed': blade_max_velocity},
    target=blade_velocity,
    rel=lambda speed, **kw : speed,
    via=lambda is_clearing, **kw : is_clearing,
    disposable=['is_clearing'],
)
blade_hg.add_edge(
    {'is_returning': blade_is_returning,
     'speed': blade_max_velocity},
    target=blade_velocity,
    rel=lambda speed, **kw : -speed,
    via=lambda is_returning, **kw : is_returning,
    disposable=['is_returning'],
)
blade_hg.add_edge(
    {'is_clearing': blade_is_clearing,
     'is_returning': blade_is_returning},
    target=blade_velocity,
    rel=lambda **kw : 0.,
    via=lambda is_clearing, is_returning, **kw :
        not is_clearing and not is_returning,
    disposable=['LEVEL', 'DISPOSE_ALL'],
)
blade_hg.add_edge(
    {'rate': blade_velocity,
     'step': timestep,
     'initial': blade_position},
    target=blade_position,
    rel=Reulerian_integration,
    index_offset=1,
    index_via=lambda rate, initial, **kw : R.Rsame(rate, initial),
    disposable=['rate', 'initial'],
)
blade_hg.add_edge(
    sources=blade_relative_position,
    target=blade_returned,
    rel=Rcalc_blade_returned,
)
blade_hg.add_edge(
    {'rel_pos':blade_relative_position},
    target=blade_at_end,
    rel=R.geq('rel_pos', 0.99),
)
blade_hg.add_edge(
    {'home': blade_home_position,
     'end': blade_end_position,
     'position': blade_position},
    target=blade_relative_position,
    rel=Rcalc_blade_rel_position,
)
blade_hg.add_edge(
    {'home': blade_home_position,
     'end': blade_end_position,
     'speed': blade_max_velocity},
    target=leveling_time,
    rel=Rcalc_leveling_time,
)