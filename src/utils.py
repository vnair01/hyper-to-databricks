def deduplicate_column_names(names):
    seen = {}
    result = []

    for name in names:
        key = name.lower()
        if key not in seen:
            seen[key] = 0
            result.append(name)
        else:
            seen[key] += 1
            result.append(f"{name}_dup{seen[key]}")

    return result
