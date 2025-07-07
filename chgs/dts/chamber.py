from constrainthg.hypergraph import Node, Hypergraph
import constrainthg.relations as R

from dts.blade import blade_hg
from dts.build_plate import plate_hg
from dts.hopper import hopper_hg
from dts.laser import laser_hg

chamber_hg = plate_hg + blade_hg + hopper_hg + laser_hg

# Nodes
chamber_temperature = chamber_hg.add_node(Node(
    label='chamber_temperature',
    description='average temperature of chamber',
    units='C',
))
layer_thickness = chamber_hg.add_node(Node(
    label='layer_thickness',
    description='thickness of build layer',
    units='mm',
))
luminosity = chamber_hg.add_node(Node(
    label='luminosity',
    description='brightness of build chamber',
    units='lumens',
))
chamber_width = chamber_hg.add_node(Node(
    label='chamber_width',
    description='width of chamber',
    units='mm'
))
chamber_length = chamber_hg.add_node(Node(
    label='chamber_length',
    description='length of chamber',
    units='mm',
))
chamber_height = chamber_hg.add_node(Node(
    label='chamber_height',
    description='height of chamber',
    units='mm',
))
bed_height = chamber_hg.add_node(Node(
    label='bed_height',
    description='height of build surface',
    units='mm',
))
bin_width = chamber_hg.add_node(Node(
    label='bin_width',
    description='width of disposal bin',
    units='mm',
))