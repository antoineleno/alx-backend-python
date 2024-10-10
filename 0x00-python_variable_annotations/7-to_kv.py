#!/usr/bin/env python3
"""to kv module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv function"""
    return (k, float(v ** 2))
