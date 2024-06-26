#!/usr/bin/env python3
""" async routine """


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    args: n and max_delay
    returns:  tasks
    """
    task = []
    for i in range(n):
        task.append(asyncio.create_task(wait_random(max_delay)))
    return await asyncio.gather(*task)
