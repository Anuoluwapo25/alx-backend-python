#!/usr/bin/env python3
"""
module task_wait_n
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args: max_delays
    Returns: tasks
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return await asyncio.gather(*tasks)
