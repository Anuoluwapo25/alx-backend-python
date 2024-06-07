#!/usr/bin/env python3
""" return sum of float list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (List[Union[int,float]]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
