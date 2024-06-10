#!/usr/bin/env python3
"""_summary"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """_summary_

    Args: max_delay
    Returns:delay
    """
<<<<<<< HEAD
    args: max_delay
    return: delay
    """
=======
>>>>>>> fc37762201a4caf388c9c21935b32e8b5fe538af
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
