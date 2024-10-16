#!/usr/bin/env python3
"""Module '1-async_comprehension.py' contains function async_comprehension """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Async generator function"""
    return [num async for num in async_generator()]
