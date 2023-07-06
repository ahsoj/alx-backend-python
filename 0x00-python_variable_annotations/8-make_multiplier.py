#!/usr/bin/env python3
"""
    typed function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return multiplier function."""
    return lambda x: x * multiplier
