import constrainthg.relations as R

def Ris_positive(*args, **kwargs)-> bool:
    """True if all arguments are positive."""
    all_args = R.extend(args, kwargs)
    return all([float(a) > 0. for a in all_args])

def Ris_negative(*args, **kwargs)-> bool:
    """True if all arguments are negative."""
    all_args = R.extend(args, kwargs)
    return all([float(a) < 0. for a in all_args])

def Reulerian_integration(rate: float, step: float, initial: float, 
                          *ar, **kw)-> float:
    """Performs a first-order Eulerian integration."""
    out = initial + rate * step
    return out

def Rlayer_finished_scanning(scan_time: float, keyframe: float, time: float, 
                             *ar, **kw)-> bool:
    """Returns true if the layer is finished scanning."""
    done = time >= scan_time + keyframe
    return done

def Rcalc_fusing_start_time(leveled: bool, progress: float, time: float,
                            prev_start: float, *ar, **kw)-> bool:
    """Returns the time that fusion began for the current layer."""
    if all([leveled, progress < 99.999]):
        return time
    return prev_start

def Rtrigger_finished_scanning(fused: float, prev_fused: float, *ar, **kw)-> bool:
    """Returns true if the layer just switched from unfused to fused."""
    unfused_to_fused = fused and not prev_fused
    return unfused_to_fused

def Rget_layers_completed(just_fused: bool, prev_layers: int,*ar, **kw)-> int:
    """Returns the number of layers completed at the current time step."""
    if just_fused:
        return prev_layers + 1
    return prev_layers

def Rcheck_laser_on(keyframe: float, time: float, finished: bool, *ar, **kw)->bool:
    """Returns true if the laser is on."""
    laser_on = time >= keyframe and not finished
    return laser_on

def Rcheck_plate_at_fusion_level(height: float, initial: float, num_layers: int,
                            step: float, tol: float, *ar, **kw)-> bool:
    """Returns True if the build plate is at a sufficient height for fusion."""
    built_offset = step * (num_layers + 1)
    fusion_height = initial + built_offset
    is_lowered = abs(height - fusion_height) < tol
    return is_lowered

def Rcheck_hopper_at_leveling_level(height: float, initial: float, num_layers: int,
                            step: float, tol: float, *ar, **kw)-> bool:
    """Returns True if the hopper is at a sufficient height for leveling."""
    built_offset = step * (num_layers)
    dispensing_height = initial + built_offset
    is_raised = abs(height - dispensing_height) < tol
    return is_raised

# def Rcheck_hopper_is_raised(height: float, prev_height: float, thickness: float,
#                                *ar, **kw)-> bool:
#     """Returns true if the hopper is raised sufficiently above the bed."""
#     is_raised = height >= prev_height + thickness
#     return is_raised

def Rcalc_vertical_position(step: float, count: int, start: float,
                            *ar, **kw)-> float:
    """Returns current position of a vertical displacing surface."""
    position = start + step * count
    return position

def Rcalc_blade_returned(rel_position: float, *ar, **kw)-> bool:
    """Returns true if the blade is in its home position."""
    returned = rel_position <= 0.
    return returned

def Rcalc_blade_rel_position(home: float, end: float, position: float,
                             *ar, **kw)-> bool:
    """Returns proportion of distance blade is from home and end positions."""
    prop = (position - home) / (end - home)
    return prop

def Rcheck_blade_is_clearing(laser: bool, plate: bool, hopper: bool, bed: bool,
                             *ar, **kw)-> bool: 
    """Returns true if the blade is clearing."""
    clearing = all([plate, hopper, not laser, not bed])
    return clearing

def Rcheck_bed_leveled(prev: bool, firing: bool, clearing: bool, at_end: bool,
                          *ar, **kw)-> bool:
    """Returns true if the bed has been leveled."""
    if firing:
        return False
    elif clearing and at_end:
        return True
    return prev

def Rcalc_leveling_time(home: float, end: float, speed: float,
                        *ar, **kw)-> float:
    """Calculates nominal time for leveling process."""
    distance = abs(home - end) * 2
    min_time = distance / speed
    adj_time = min_time * 1.2
    return adj_time

def Rcalc_build_time(scan_times: list, leveling_time: float,
                     *ar, **kw)-> float:
    """Calculates the total time to build the part."""
    build_time = sum(scan_times) + leveling_time * len(scan_times)
    return build_time