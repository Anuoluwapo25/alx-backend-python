#!/usr/bin/env python3
"""_summary_"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    return lambda x: x * multiplier
