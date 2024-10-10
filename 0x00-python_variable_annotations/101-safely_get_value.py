#!/usr/bin/env python3
"""safely_get_value module"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''safely_get_value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
