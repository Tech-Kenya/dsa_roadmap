from typing import List

def merge(list1:List[int], list2:List[int]) -> List[int]:
    left = right = 0
    m, n = len(list1), len(list2)
    merged = []

    while left < m and right < n:
        if list1[left] < list2[right]:
            merged.append(list1[left])
            left += 1
        else:
            merged.append(list2[right])
            right += 1
    
    # remaining elements in the two lists
    while left < m:
        merged.append(list1[left])
        left += 1
    
    while right < n:
        merged.append(list2[right])
        right += 1
        
    return merged


# SP: O(1) - if no need for an extra space
# def merge(list1:List[int], list2:List[int]) -> List[int]:
#     
#     left, right = len(list1), len(list2)
#     last = len(list1) + len(list2) - 1

#     while left < len(list1) and right < len(list2):
#         if list1[left] < list2[right]:
#             list1[last] = list1[left]
#             left -= 1
#         else:
#             list1[last] = list2[right]
#             right -= 1
#         left -= 1


#     return list1