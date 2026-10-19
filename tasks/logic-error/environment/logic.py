from typing import List

def snap(list: List[int]):
    """Simple function that takes a integer List of any length and returns the bottom half (rounded down) of integers.
    If the list is empty, an empty list should be returned."""

    max = list[-1]
    for num in list:
        if (num > max):
            list.remove(num)
    
    return list