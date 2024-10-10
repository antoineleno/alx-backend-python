#!/usr/bin/env python3
"""safely_get_value module"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """safely_get_value function"""
    if key in dct:
        return dct[key]
    else:
        return default
