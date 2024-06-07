#!/usr/bin/env python3
"""type annotations"""


from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    args: lst:iterable
    """
    return [(i, len(i)) for i in lst]
