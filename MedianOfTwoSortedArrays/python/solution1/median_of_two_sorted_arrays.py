#!/usr/bin/python3
from typing import List

# Solution 1 to the problem of find the media of two already sorted list
#
# First it merge the two list, then it gets the element (or elements) of the middle


def merge_sorted_list(l1: List[int], l2: List[int]) -> List[int]:
    """Merge two already sorted lists, so that the returned list is sorted

    :param l1: First list. It must be already sorted
    :param l2: Second list. It must be already sorted
    :returns: The list of the sorted values of l1 and l2
    """
    merge_list = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merge_list.append(l1[i])
            i += 1
        else:
            merge_list.append(l2[j])
            j += 1

    while i < len(l1):
        merge_list.append(l1[i])
        i += 1

    while j < len(l2):
        merge_list.append(l2[j])
        j += 1

    return merge_list


def median_two_sorted_list(l1: List[int], l2: List[int]) -> float:
    """Returns the median of the values in l1 and l2

    :param l1: First sorted list
    :param l2: Second sorted list

    :returns: Median of the values in l1 and l2
    """
    merge_list = merge_sorted_list(l1, l2)
    mid = len(merge_list) // 2

    if len(merge_list) % 2 == 1:
        return merge_list[mid]
    else:
        m1 = merge_list[mid-1]
        m2 = merge_list[mid]
        return (m1 + m2) / 2
