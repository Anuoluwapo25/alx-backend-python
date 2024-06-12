#!/usr/bin/env python3
""" async_comprehension """

import asyncio
import random
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Args: lists
    Returns: coroutine list of float
    """
<<<<<<< HEAD
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
=======
    num_list = [i async for i in async_generator()]
    return num_list
>>>>>>> 0d40e3e3868c73aa9cc476046943d49b0053e928
