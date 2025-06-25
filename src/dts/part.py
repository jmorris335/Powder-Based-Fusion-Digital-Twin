from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

part_hg = Hypergraph()

# Nodes
timestep = part_hg.add_node(Node(
    label='timestep',
    description='smallest time unit considered',
    units='s',
))
time = part_hg.add_node(Node(
    label='time',
    description='current time of process',
    units='s',
))
part_name = part_hg.add_node(Node(
    label='part_name',
    description='name of part',
))
part_height = part_hg.add_node(Node(
    label='part_height',
    description='height of part',
))
build_time = part_hg.add_node(Node(
    label='build_time',
    description='time to build part',
    units='s',
))
build_progress = part_hg.add_node(Node(
    label='build_progress',
    description='proportion of build completed',
    units='%',
))

# Edges
part_hg.add_edge(
    {'time': time,
     'total': build_time},
    target=build_progress,
    rel=lambda time, total, **kw : time / total,
    disposable=['time'],
)