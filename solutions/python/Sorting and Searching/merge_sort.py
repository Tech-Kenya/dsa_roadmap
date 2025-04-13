from typing import List, Optional
from merge import merge

def merge_sort(arr: List[int]) -> Optional[callable]:
    if len(arr) == 1: return arr

    mid_point = len(arr)//2

    left_half = merge_sort(arr[:mid_point])
    right_half = merge_sort(arr[mid_point:])

    return merge(left_half, right_half)



if __name__ == "__main__":
    arr = [8, 40, 6, 4, 11, 5, 7]
    actual = [4, 5, 6, 7, 8, 11, 40]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    assert sorted_arr == actual, 'not sorted!'

    arr = [6]
    actual = [6]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    assert sorted_arr == actual, 'not sorted!'


# TC: O(n log n)
# SP: O(n) - if implemented well, we could end up with O(1)