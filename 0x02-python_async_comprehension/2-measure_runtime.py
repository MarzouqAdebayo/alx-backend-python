#!/usr/bin/env python3
"""Module '2-measure_runtime.py' contains measure_time """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of coroutines"""
    start = time.perf_counter()
    _ = asyncio.run(async_comprehension())
    end = time.perf_counter() - start
    return end
