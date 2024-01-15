#!/usr/bin/env python3
import asyncio
"""asynchronous coroutine that takes in an integer argument"""


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    Args:
        max_delay (int, optional): [description]. Defaults to 10.
    Returns:
        float: random delay between 0 and max_delay
    """
    import random
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
