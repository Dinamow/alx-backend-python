#!/usr/bin/python3
from typing import List, Tuple, Union
"""zoom_array module"""


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)