#!/usr/bin/env python3
"""Module '2-measure_runtime.py' contains measure_time """
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of coroutines"""
    start = time.perf_counter()
    _ = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
