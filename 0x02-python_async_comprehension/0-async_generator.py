#!/usr/bin/env python3
""" async_comprehension """


import asyncio
import random
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """
    Args: async function
    Return: random numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
