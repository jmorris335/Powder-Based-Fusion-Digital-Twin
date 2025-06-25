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
chamber_height = Node(
    label='chamber_height',
    description='height of chamber',
    units='mm',
)
bed_height = Node(
    label='bed_height',
    description='height of build surface',
    units='mm',
)
bin_width = Node(
    label='bin_width',
    description='width of disposal bin',
    units='mm'
)