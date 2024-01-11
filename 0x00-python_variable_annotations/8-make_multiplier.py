"""make_multiplier Module"""


def make_multiplier(multiplier: float) -> callable:
    """make_multiplier: takes a float multiplier and returns a function that
    multiplies a float by multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        callable: function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier