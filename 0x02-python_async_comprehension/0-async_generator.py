#!/usr/bin/env python3
"""async_generator module file for 0x02-python_async_comprehension project"""


async def async_generator():
    """async_generator function"""
    import random
    for i in range(10):
        yield random.uniform(0, 10)
