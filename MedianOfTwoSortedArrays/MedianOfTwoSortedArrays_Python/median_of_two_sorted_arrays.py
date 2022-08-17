from math import ceil, floor


def find_median_sorted_list(list1, list2):
    if len(list1) + len(list2) % 2 == 1:
        k = (len(list1) + len(list2)) // 2
        return find_k_element_sorted_lists(list1, list2, k)
    else:
        k = (len(list1) + len(list2)) / 2
        k1 = floor(k)
        result1 = find_k_element_sorted_lists(list1, list2, k1)

        k2 = ceil(k)
        result2 = find_k_element_sorted_lists(list1, list2, k2)

        return (result1 + result2) / 2


def find_k_element_sorted_lists(list1, list2, k):
    if len(list1) == 0:
        return list2[k]
    if len(list2) == 0:
        return list1[k]

    if len(list1) == 1 and len(list2) == 1:
        if k == 0:
            if list1[0] > list2[0]:
                return list2[0]
            else:
                return list1[0]
        else:
            if list1[0] > list2[0]:
                return list1[0]
            else:
                return list2[0]

    a = len(list1) // 2
    b = len(list2) // 2

    if k <= len(list1[:a]) + len(list2[:b]) + 1:
        if list1[a] > list2[b]:
            return find_k_element_sorted_lists(list1[:a], list2, k)
        else:
            return find_k_element_sorted_lists(list1, list2[:b], k)

    else:
        if list1[a] > list2[b]:
            return find_k_element_sorted_lists(list1, list2[b+1:], k-(b+1))
        else:
            return find_k_element_sorted_lists(list1[a+1:], list2, k-(a+1))


def main():
    print(find_k_element_sorted_lists([1, 3, 4], [2, 5], 3))


if __name__ == "__main__":
    main()
