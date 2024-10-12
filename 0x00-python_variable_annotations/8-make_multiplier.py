#!/usr/bin/env python3
"""Module '8-make_multiplier.py' contains make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies with multiplier"""

    def F(x: float) -> float:
        """Mulitplies a number by  multiplier"""
        return x * multiplier

    return F
