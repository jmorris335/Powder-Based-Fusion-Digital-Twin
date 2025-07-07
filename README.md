# Powder Based Fusion Digital Twin
Digital Twin for a Powder-Bed Fusion (PBF) additive manufacturing process.

https://github.com/jmorris335/Powder-Based-Fusion-Digital-Twin/blob/c9d45b2103ba43621eb44225002483fd4a7983b3/media/pbf%20process%20animation.gif

# Running
## General Setup
Package dependencies ([ConstraintHg](https://constrainthg.readthedocs.io/en/latest/index.html) and Matplotlib) are in the `requirements.txt` file. After downloading the repo and initializing your virtual environment, just call 

```
pip install -r requirements.txt
```

## Constraint Hypergraph Examples
The CHG examples live in the `chgs` directory and are called from the `caller.py` script at its base. Each digital twin is in the `chgs/dts` directory, and is a collection of nodes (parameters) and edges (relationships) forming a constraint hypergraph. You can run these individually by calling the `solve()` method on any of the individual hypergraphs. For instance, to execute the Hopper digital twin you could run the following:

```python
inputs = dict(
    hopper_x_position=400,
    hopper_initial_y_position=140,
    hopper_width=200,
    material_density=0.0027,
)

hopper_hg.solve(material_mass, inputs)
```
Here the inputs are provided as a dict with the labels of a node as keys pointing to the values given to each input. The `solve()` method comes from the ConstraintHg package and takes a target node as its first parameter (the output), and the inputs as its second parameter. Other options are described in the [documentation](https://constrainthg.readthedocs.io/en/latest/constrainthg.html#constrainthg.hypergraph.Hypergraph.solve).

Note that `hopper_hg` is the constraint hypergraph created in the `hopper.py` digital twin module. You can add hypergraphs to combine them using a dumb union across their shared nodes, as in `dtALL = dt1_hg + dt2_hg`.

To visualize the full PBF machine, use the methods in `aux/plotter.py`:
- `visualization_caller()` plots a static image of the PBF machine.
- `animation_caller()` animates a process of the PBF machine.

# Information
Authors: [John Morris](https://orcid.org/0009-0005-6571-1959), [Duncan Gibbons](https://orcid.org/0000-0002-7641-4221), [Joe Gregory](https://orcid.org/0000-0002-4027-6314)  
License: MIT License