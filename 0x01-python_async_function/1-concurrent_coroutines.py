#!/usr/bin/env python3
"""concurrent_coroutines"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all delays"""
    delay = await asyncio.gather(
        *(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay)
