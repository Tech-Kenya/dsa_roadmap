#!/usr/bin/python3
import random

def maximum_and_minimum_element(array: list[int]) -> tuple[int, int]:
    """
    Takes in a list of integers and returns a tuple of integers of the mimimum and maximum elements.

    Args:
        array (list[int]): A list of integers.

    Returns:
        tuple(int, int): The minimum and maximum element of the list.
    """
    return (max(array), min(array))

# Generate list elements randomly

random_list = [random.randint(1, 100) for _ in range(10)]
max_element, min_element = maximum_and_minimum_element(random_list)
print(f"The list elements are : {random_list}.")
print(f"The maximum element is: {max_element}.\nThe minimum element is: {min_element}.")
