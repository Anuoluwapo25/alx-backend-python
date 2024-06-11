#!/usr/bin/env python3
"""
module task_wait_n
"""


import asyncio
from typing import List


task_wait_random = __import__('0-basic_async_syntax').task_wait_random


async def task_wait_random(max_delay: int) -> float:
"""
    Simulates a random wait with a maximum delay.

    Args:
        max_delay (float): The maximum amount of time to wait (in seconds).

    Returns:
        float: The actual delay used, which will be a random value between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args: max_delays
    Returns: tasks
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return await asyncio.gather(*tasks)
