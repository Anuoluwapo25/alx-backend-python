""" async_comprehension """

import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Args: lists
    Returns: coroutine runtime
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    totalrun = end - start
    return totalrun
