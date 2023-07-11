#!/usr/bin/python3
"""async comprehension"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """return list of float from generator function"""
    return [i async for i in async_generator()]
