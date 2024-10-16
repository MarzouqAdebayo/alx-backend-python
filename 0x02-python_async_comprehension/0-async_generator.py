#!/usr/bin/env python3
"""Module '0-async_generator.py' contains function async_generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator function"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
