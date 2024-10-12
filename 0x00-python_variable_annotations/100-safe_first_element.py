#!/usr/bin/env python3
"""Module '100-safe_first_element.py'"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Gets the first element of the sequence if it exists"""
    if lst:
        return lst[0]
    else:
        return None
