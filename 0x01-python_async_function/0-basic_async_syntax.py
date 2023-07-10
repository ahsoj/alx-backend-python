#!/usr/bin/env python3
"""basic asyncio function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random amount of time between zero and max delay"""
    wait_time = random.random() * (max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
