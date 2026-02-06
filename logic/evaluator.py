def extract_variables(expr: str):
    return sorted(set(c for c in expr if c.isalpha()))


def evaluate(expr: str, variables: list, values: tuple):
    context = dict(zip(variables, values))
    return eval(expr, {}, context)


def classify(results: list):
    if all(results):
        return "Tautologia"
    elif not any(results):
        return "Contradição"
    return "Contingência"
