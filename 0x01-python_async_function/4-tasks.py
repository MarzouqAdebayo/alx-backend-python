#!/usr/bin/env python3
"""Module '4-tasks.py' contains function task_wait_n """
from typing import List
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple coroutines at the same time with async"""
    result = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n)))
    return sorted(result)
