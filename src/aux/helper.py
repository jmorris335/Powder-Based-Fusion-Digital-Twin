def print_vals(t, key: str):
    """Prints all the values associated with the solved TNode."""
    if key not in t.values:
        pass
        # print(f'No values found for {key}')
    else:
        out = f'{key}: '
        for val in t.values[key]:
            if isinstance(val, float):
                val = f'{val:.2f}'
                if val[-3:] == '.00':
                    val = val[:-2]
            out += f'{val}, '
        print(out)