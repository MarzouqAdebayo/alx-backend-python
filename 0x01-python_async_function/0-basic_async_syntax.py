#!/usr/bin/env python3
"""Module '0-basic_async_syntax' contains function wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function to delay for some time"""
    delay_time = random.uniform(max_delay)
    await asyncio.seep(delay_time)
    return delay_time
