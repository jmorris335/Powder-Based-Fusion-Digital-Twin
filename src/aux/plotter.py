from constrainthg import Hypergraph
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import inspect

def visualization_caller(hg: Hypergraph):
    """Plots the PBF machine from the hypergraph."""
    kwargs = filter_dict_to_kwargs(plot_pbf, hg.nodes)
    kwargs = {k : n.static_value for k, n in kwargs.items()}
    plot_pbf(**kwargs)

def filter_dict_to_kwargs(func, data: dict):
    """Return key-value pairs from data that match func's keyword arguments."""
    sig = inspect.signature(func)
    keyword_types = (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY)
    valid_keys = [
        func_kw for func_kw, param in sig.parameters.items() 
        if param.kind in keyword_types
    ]
    kwargs = {
        data_key: data_val for data_key, data_val in data.items() 
        if data_key in valid_keys
    }
    return kwargs

def get_blade_patch(blade_position: float, bed_height: float, height: float, 
                    width: float=None):
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
    plate = Rectangle(xy, width, height, fill=False, ec='#008822', lw=2)
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

def get_laser_lines(x_center: float, y_top: float, height: float):
    """Returns a list of lines indicating an operating laser."""
    spread = height * 0.3
    num_lines = 3
    gap = spread / (num_lines - 1)
    x_ends = [x_center - spread / 2 + gap * i for i in range(num_lines)]
    lines = []
    for x_end in x_ends:
        lines.extend(plt.plot([x_center, x_end], [y_top, y_top - height], 'r-', lw=2))
    return lines

def plot_pbf(chamber_width: float, chamber_height: float, bed_height: float,
             bin_width: float,
             blade_position: float, blade_height: float, 
             hopper_x_position: float, hopper_y_position: float, hopper_width: float, 
             build_plate_x_position: float, build_plate_y_position: float, 
             build_plate_width: float,
             build_progress: float=None, time: float=None, laser_is_on: bool=False,
             tol: float=0.1):
    """Plots the powder-bed fusion machine."""
    fig, ax = plt.subplots()
    ax.add_collection(get_chamber_patches(chamber_width, chamber_height, bed_height, bin_width, tol))
    ax.add_patch(get_blade_patch(blade_position, bed_height, blade_height))
    ax.add_patch(get_hopper_patch(hopper_x_position, hopper_y_position, hopper_width, bed_height - hopper_y_position))
    ax.add_patch(get_build_plate_patch(build_plate_x_position, build_plate_y_position, build_plate_width, bed_height - build_plate_y_position))
    
    if build_progress is not None:
        text_x = build_plate_x_position + build_plate_width / 2
        text_y = build_plate_y_position + (bed_height - build_plate_y_position) / 2
        ax.text(
            x=text_x, y=text_y,
            s=f'Build Progress:\n{build_progress:.0f}%',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10,
    )
        
    if time is not None:
        fontsize = 11
        ax.text(
            x = 0, y = 0 - fontsize / 72 - tol,
            s=f'Time: {time:.2f} s',
            fontsize=fontsize,
        )

    if laser_is_on:
        x_center = chamber_width / 2
        y_top = chamber_height
        for line in get_laser_lines(x_center, y_top, y_top - bed_height):
            ax.add_line(line)
    
    ax.set_xlim(-tol, chamber_width + tol)
    ax.set_ylim(-tol, chamber_height + tol)
    ax.set_aspect('equal')
    ax.axis('off')
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
        time=3.71,
        build_progress=81.3,
        laser_is_on=True,
        tol=0.1,
    )