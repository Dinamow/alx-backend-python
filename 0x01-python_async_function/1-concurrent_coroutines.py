#!/usr/bin/env python3
"""Asynchronous module with wait_n function"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """waits for random delay and returns list of delays in ascending order
    Args:
        n (int): number of times to call wait_random
        max_delay (int): max delay passed to wait_random
    Returns:
        list: list of delays in ascending order
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays
