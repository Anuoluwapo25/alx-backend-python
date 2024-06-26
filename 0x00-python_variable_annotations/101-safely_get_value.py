#!/usr/bin/env python3
"""type annotations"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """_
    Args:dct: (Mapping)
    Return:Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
