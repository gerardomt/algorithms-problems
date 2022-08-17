import unittest
import median_of_two_sorted_arrays as mtsa


class TestMedianSortedArrays(unittest.TestCase):
    def test_find_k_element_list1_empty(self):
        result = mtsa.find_k_element_sorted_lists([], [1], 0)
        self.assertEqual(result, 1)

    def test_find_k_element_list2_empty(self):
        result = mtsa.find_k_element_sorted_lists([1, 2, 3], [], 1)
        self.assertEqual(result, 2)

    def test_find_k_element_all_mayor(self):
        result = mtsa.find_k_element_sorted_lists([1, 2, 3], [4, 5, 6], 3)
        self.assertEqual(result, 4)

    def test_find_k_element_repeated_element(self):
        result = mtsa.find_k_element_sorted_lists([1, 1, 1], [1, 1, 1], 3)
        self.assertEqual(result, 1)

    def test_find_median_1(self):
        result = mtsa.find_median_sorted_list([1, 3], [2])
        self.assertEqual(result, 2.0)

    def test_find_median_2(self):
        result = mtsa.find_median_sorted_list([1, 2], [3, 4])
        self.assertEqual(result, 2.5)


if __name__ == '__main__':
    unittest.main()
