from pytesting_cicd.functions import add, subtract


def run_functions(a: int, b: int, c: int):
    result = add(add(a, b), c)
    result = subtract(result, c)
    result = subtract(result, b)
    result = subtract(result, a)
    return result
