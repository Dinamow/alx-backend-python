#!/usr/bin/env python3
"""measure_runtime module file for 0x02-python_async_comprehension project"""
import asyncio
import time


async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """
    measure_runtime function
    Returns:
        float: [description]
    """
    start_time = time.time()
    await asyncio.gather(*(async_generator() for i in range(4)))
    end_time = time.time()
    return end_time - start_time
