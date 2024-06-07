#!/usr/bin/env python3
"""typed"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args: lst
    Returns: lst[0]
    """
    if lst:
        return lst[0]
    else:
        return None
