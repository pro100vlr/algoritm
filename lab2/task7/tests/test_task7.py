import unittest
from lab2.task7.src.task7 import max_subarray_with_indices

class TestMaxSubarrayWithIndices(unittest.TestCase):
    def test_should_find_maximum_subarray_in_mixed_numbers(self):

        # given
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_result = (6, 3, 6)  # Максимальная сумма: 6, подмассив: [4, -1, 2, 1]

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_single_element_when_all_negative_numbers(self):

        # given
        arr = [-8, -3, -6, -2, -5, -4]
        expected_result = (-2, 3, 3)  # Максимальный подмассив — элемент -2 сам по себе

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_entire_array_when_all_positive_numbers(self):
        
        # given
        arr = [1, 2, 3, 4, 5]
        expected_result = (15, 0, 4)  # Сумма всех элементов: 15

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_maximum_subarray_with_single_element(self):

        # given
        arr = [42]
        expected_result = (42, 0, 0)  # Один элемент: максимальная сумма — сам элемент

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_maximum_subarray_in_array_with_zeroes(self):

        # given
        arr = [0, -3, 5, -1, 2, -2, 0, 3]
        expected_result = (7, 2, 7)  # Максимальная сумма: 7, подмассив: [5, -1, 2, -2, 0, 3]

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_result_for_large_negative_prefix(self):

        # given
        arr = [-10, -5, 4, 6, -2, 1]
        expected_result = (10, 2, 3)  

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_correct_result_when_array_contains_multiple_max_subarrays(self):
        
        # given
        arr = [3, -2, 3, -2, 3]
        expected_result = (5, 0, 4)  

        # when
        result = max_subarray_with_indices(arr)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
