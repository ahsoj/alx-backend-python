#!/usr/bin/env python3
"""
    typed function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of a list[floats]"""
    return float(sum(input_list))
