import itertools

def generate(variables: list):
    return list(itertools.product([False, True], repeat=len(variables)))
