#!/usr/bin/env python3
"""5-sum_list module"""
from typing import List


type type_list = List[float]


def sum_list(input_list: type_list) -> float:
    """summ_list function

    Args:
        input_list (type_list): a list of numbers

    Returns:
        float: The sum of all values in the list
    """
    return sum(input_list)
