#!/usr/bin/python3
from typing import Mapping, Any, Union, TypeVar
"""safely_get_value module"""

T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None)\
                     -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default