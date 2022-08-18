#!/usr/bin/python3

# Solution 1 to the problem of find the media of two already sorted list
#
# First it merge the two list, then it gets the element (or elements) of the middle

def merge_sorted_list(l1, l2):
    """Merge two already sorted lists, so that the returned list is sorted"""
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
