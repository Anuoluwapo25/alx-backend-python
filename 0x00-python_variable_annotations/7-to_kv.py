#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""


from typing import Union, Tuple
from math import pow


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (str): _description_
        v (typing.Union): _description_

    Returns:
        tuple: _description_
    """
    return (k, pow(v, 2))
