#!/usr/bin/env python3
"""100 -safe first element module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_elements function
    """
    if lst:
        return lst[0]
    else:
        return None
