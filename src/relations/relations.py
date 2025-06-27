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
                          *args, **kwargs):
    """Performs a first-order Eulerian integration."""
    out = initial + rate * step
    return out

def Rlayer_finished_scanning(scan_time: float, keyframe: float, time: float, 
                             *args, **kwargs)-> bool:
    """Returns true if the layer is finished scanning."""
    done = time >= scan_time + keyframe
    return done

def Rcheck_start_fusing(leveled: bool, no_blade: bool, progress: float, 
                        *args, **kwargs)-> bool:
    """Returns true if the PBF machine is prepared to start fusion."""
    if not all(leveled, no_blade):
        return False
    ready = progress < 99.999
    return ready

def Rtrigger_finished_scanning(fused: float, prev_fused: float, 
                             *args, **kwargs)-> bool:
    """Returns true if the layer just switched from unfused to fused."""
    unfused_to_fused = fused and not prev_fused
    return unfused_to_fused

def Rcheck_laser_on(keyframe: float, time: float, finished: bool, 
                    *args, **kwargs)->bool:
    """Returns true if the laser is on."""
    laser_on = time >= keyframe and not finished
    return laser_on

def Rcheck_if_plate_is_lowered(height: float, bed_height: float, thickness: float, 
                               *args, **kwargs)-> bool:
    """Returns true if the plate is lowered sufficiently below the bed."""
    is_lowered = height <= bed_height - thickness
    return is_lowered

def Rcheck_if_hopper_is_raised(height: float, prev_height: float, thickness: float,
                               *args, **kwargs)-> bool:
    """Returns true if the hopper is raised sufficiently above the bed."""
    is_raised = height >= prev_height + thickness
    return is_raised

def Rcalc_vertical_position(step: float, count: int, start: float,
                            *args, **kwargs)-> float:
    """Returns current position of a vertical displacing surface."""
    position = start + step + count
    return position

def Rcalc_blade_returned(rel_position: float, *args, **kwargs)-> bool:
    """Returns true if the blade is in its home position."""
    returned = rel_position <= 0.
    return returned

def Rcalc_blade_rel_position(home: float, end: float, position: float,
                             *args, **kwargs)-> bool:
    """Returns proportion of distance blade is from home and end positions."""
    prop = (position - home) / (end - home)
    return prop

def Rcheck_if_bed_cleared(prev: bool, firing: bool, clearing: bool, at_end: bool,
                          *args, **kwargs)-> bool:
    """Returns true if the bed has been cleared."""
    if firing:
        return False
    elif clearing and at_end:
        return True
    return prev