#!/usr/bin/env python3
"""async genrator"""
import asyncio
import random


async def async_generator():
    """Async generator function."""
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
