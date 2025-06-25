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