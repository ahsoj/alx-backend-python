#!/usr/bin/env python3
"""async genrator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator function."""
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
