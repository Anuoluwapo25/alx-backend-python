#!/usr/bin/env python3
"""type checking_"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Args:
        lst (Tuple)
    Returns: tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom1 = zoom_array(array)

zoom2 = zoom_array(array, int(3.0))
