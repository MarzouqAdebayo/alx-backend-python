#!/usr/bin/env python3
"""Module '1-concurrent_coroutines.py' contains function wait_n"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple coroutines at the same time with async"""
    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return result
