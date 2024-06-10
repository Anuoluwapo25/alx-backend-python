#!/usr/bin/env python3
"""
asynchronous coroutine
"""

import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    args: max_delay
    return: 
    """
    delay = random.uniform(0, max_delay)
    await.asyncio.sleep(delay)
    return delay    