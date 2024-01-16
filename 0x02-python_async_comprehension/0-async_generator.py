#!/usr/bin/env python3
"""async_generator module file for 0x02-python_async_comprehension project"""
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator function
    Returns:
        Generator[float, None, None]: [description]
    """
    import random
    for i in range(10):
        yield random.uniform(0, 10)
