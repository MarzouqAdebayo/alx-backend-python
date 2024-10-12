#!/usr/bin/env python3
"""Module '7-to_kv.py' contains function to_kv"""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Square a number and returns a tuple"""
    return (k, v * v)
