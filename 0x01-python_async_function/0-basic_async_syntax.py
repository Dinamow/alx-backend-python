#!/usr/bin/env python3
import asyncio

async def wait_random(max_delay = 10):
    """Asynchronous coroutine that takes in an integer argument
    Args:
        max_delay (int, optional): [description]. Defaults to 10.
    Returns:
        float: random delay between 0 and max_delay
    """
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
