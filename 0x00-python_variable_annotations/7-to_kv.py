#!/usr/bin/env python3
"""
    typed function
"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """return a tuple"""
    return (k, float(v**2))
