from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from relations.relations import *

laser_hg = Hypergraph()

# Nodes
laser_is_on = laser_hg.add_node(Node(
    label='laser_is_on',
    description='true if laser is currently firing',
    units='Boolean',
))