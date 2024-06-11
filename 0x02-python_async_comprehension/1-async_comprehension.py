""" async_comprehension """

import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension()  -> List[float]:
    """
    Args: lists
    Returns: coroutine
    """
    return [i async for i in async_generator()]