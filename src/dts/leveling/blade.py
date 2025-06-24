from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

blade_hg = Hypergraph()

# Nodes
blade_name = Node('blade_name', description='name for blade')
blade_type = Node('blade_type', description='type of blade')
blade_angle = Node('blade_angle', description='angle for blade', units='degrees')
