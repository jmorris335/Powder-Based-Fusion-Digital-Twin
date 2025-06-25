from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

chamber_hg = Hypergraph()

# Nodes
chamber_temperature = Node(
    label='chamber_temperature',
    description='average temperature of chamber',
    units='C',
)
layer_thickness = Node(
    label='layer_thickness',
    description='thickness of build layer',
    units='mm',
)
luminosity = Node(
    label='luminosity',
    description='brightness of build chamber',
    units='lumens',
)
chamber_width = Node(
    label='chamber_width',
    description='width of chamber',
    units='mm'
)
chamber_length = Node(
    label='chamber_length',
    description='length of chamber',
    units='mm',
)