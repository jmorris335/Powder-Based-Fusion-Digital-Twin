from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

pbf_hg = Hypergraph()

# Nodes
build_time = Node(
    label='build_time',
    description='time to build part',
    units='s',
)
amount_in_stock = Node(
    label='amount_in_stock',
    description='amount of material remaining in stock',
    units='g',
)
current_material = Node(
    label='current_material',
    description='name of material currently loaded in chamber',
)