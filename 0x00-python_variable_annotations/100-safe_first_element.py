#!/usr/bin/env python3
from typing import Any, Sequence, Union
"""safe_first_element module"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element: takes a list and returns its first element
    Args:
        lst ([type]): list of any type
    Returns:
        [type]: first element of lst
    """
    if lst:
        return lst[0]
    else:
        return None
