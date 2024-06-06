# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):
    if x < 0 or y < 0:
        raise Exception(f"x and y can not be less than 0. Given x: '{x}', y: '{y}")

    if x > 100 or y > 100:
        raise Exception(f"x and y can not be greater than 100. Given x: '{x}', y: '{y}")
    return x + y



