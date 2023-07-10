#!/usr/bin/env python3
"""concurrent_coroutines tasks"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all delays"""
    delay = await asyncio.gather(
        *(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay)
