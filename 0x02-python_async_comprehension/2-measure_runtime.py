#!/usr/bin/env python3
"""Module '2-measure_runtime.py' contains measure_time """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_time() -> float:
    """Measure the runtime of coroutines"""
    start = time.Time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.Time() - start
