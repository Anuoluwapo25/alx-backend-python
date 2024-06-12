""" async_comprehension """


import time
import asyncio
from datetime import datetime

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Args: lists
    Returns: coroutine runtime
    """
    start = datetime.now()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    total_run  = datetime.now() - start).total_seconds()
    return total_run
