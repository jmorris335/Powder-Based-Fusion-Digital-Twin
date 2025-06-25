import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.collections import PatchCollection

def get_blade_patch(blade_position: float, bed_height: float, height: float, width: float=None):
    """Returns a patch for the blade."""
    if width is None:
        width = height * 0.3
    xy = (blade_position, bed_height)
    blade = Rectangle(xy, width, height, fc='#335368', ec='k')
    return blade

def get_build_plate_patch(x_position: float, y_position: float, width: float, 
                          height: float):
    """Returns a patch for the build plate."""
    xy = (x_position, y_position)
    plate = Rectangle(xy, width, height, fill=False, ec='r', lw=2)
    return plate

def get_hopper_patch(x_position: float, y_position: float, width: float, height: float):
    """Returns a patch for the hopper."""
    xy = (x_position, y_position)
    hopper = Rectangle(xy, width, height, fill=False, ec='b', lw=2)
    return hopper

def get_chamber_patches(width: float, height: float, 
                      surface_height: float, bin_width: float, tol: float=0.1):
    """Returns a patch for the chamber."""
    chamber = Rectangle((0, 0), width, height)
    bin = Rectangle((tol, tol), bin_width-tol, surface_height-tol)
    return PatchCollection([chamber, bin], fc='white', ec='k', lw=2)

def plot_pbf(chamber_width: float, chamber_height: float, bed_height: float,
             bin_width: float,
             blade_position: float, blade_height: float, 
             hopper_x_position: float, hopper_y_position: float, hopper_width: float, 
             build_plate_x_position: float, build_plate_y_position: float, 
             build_plate_width: float, tol: float=0.1):
    """Plots the powder-bed fusion machine."""
    fig, ax = plt.subplots()
    ax.add_collection(get_chamber_patches(chamber_width, chamber_height, bed_height, bin_width, tol))
    ax.add_patch(get_blade_patch(blade_position, bed_height, blade_height))
    ax.add_patch(get_hopper_patch(hopper_x_position, hopper_y_position, hopper_width, bed_height - hopper_y_position))
    ax.add_patch(get_build_plate_patch(build_plate_x_position, build_plate_y_position, build_plate_width, bed_height - build_plate_y_position))
    ax.set_xlim(-tol, chamber_width + tol)
    ax.set_ylim(-tol, chamber_height + tol)
    ax.set_aspect('equal')
    plt.show()

if __name__ == '__main__':
    plot_pbf(
        chamber_width=6.1,
        chamber_height=4.1,
        bed_height=3.,
        bin_width=2.,
        blade_position=5.8,
        blade_height=0.5,
        hopper_x_position=4,
        hopper_y_position=1.4,
        hopper_width=2,
        build_plate_x_position=2,
        build_plate_y_position=2.1,
        build_plate_width=2,
        tol=0.1,
    )