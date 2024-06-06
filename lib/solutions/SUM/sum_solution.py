# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or y < 0:
        raise Exception(f"x and y can not be less than 0. Given x: '{x}', y: '{y}")
    return x + y


