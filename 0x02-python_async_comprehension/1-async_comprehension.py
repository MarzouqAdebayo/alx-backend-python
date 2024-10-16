#!/usr/bin/env python3
"""Module '1-async_comprehension.py' contains function async_comprehension """
from typing import Generator

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Async generator function"""
    return [i async for i in async_generator()]
