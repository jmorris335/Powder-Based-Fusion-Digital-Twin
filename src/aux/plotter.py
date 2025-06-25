from constrainthg import Hypergraph
from src.relations.visualization import plot_pbf
import inspect

def plot_pbf_wrapper(hg: Hypergraph):
    """Plots the PBF machine from the hypergraph."""
    kwargs = filter_dict_to_kwargs(plot_pbf, hg.nodes)
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