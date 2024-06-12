#!/usr/bin/env python3
""" async_comprehension """


import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start = perf_counter()
    numbers_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*numbers_list)
    return perf_counter() - start