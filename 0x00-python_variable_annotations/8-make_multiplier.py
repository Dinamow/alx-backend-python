#!/usr/bin/env python3
from typing import Callable
"""make_multiplier Module"""


def make_multiplier(multiplier: float) -> Callable:
    """make_multiplier: takes a float multiplier and returns a function that
    multiplies a float by multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        callable: function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
