#!/usr/bin/env python3
"""measure_runtime"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    s_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.perf_counter() - s_time
    total_time = e_time / n
    return total_time
