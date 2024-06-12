""" async_comprehension """

import asyncio
import random
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Args: lists
    Returns: coroutine list of float
    """
    return [await value for value in async_generator()]
