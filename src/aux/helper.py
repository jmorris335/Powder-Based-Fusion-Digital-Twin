def print_vals(t, key: str):
    """Prints all the values associated with the solved TNode."""
    if key not in t.values:
        print(f'No values found for {key}')
    else:
        print(f'{key}: {t.values[key]}')