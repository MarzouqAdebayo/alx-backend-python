#!/usr/bin/env python3
"""Module '101-safely_get_value.py'"""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Get a value from a dict using a key"""
    if key in dct:
        return dct[key]
    else:
        return default
