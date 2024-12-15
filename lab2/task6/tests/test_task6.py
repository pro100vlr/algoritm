import unittest
from lab2.task6.src.task6 import find_max_crossing_subarray, find_maximum_subarray

class TestFindMaximumSubarray(unittest.TestCase):
    def test_should_find_max_crossing_subarray(self):

        # given
        prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        low = 0
        mid = 4
        high = 8
        expected_result = (3, 6, 6)  # Подмассив [4, -1, 2, 1] с суммой 6

        # when
        result = find_max_crossing_subarray(prices, low, mid, high)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_maximum_subarray(self):

        # given
        prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        low = 0
        high = len(prices) - 1
        expected_result = (3, 6, 6)  # Подмассив [4, -1, 2, 1] с суммой 6

        # when
        result = find_maximum_subarray(prices, low, high)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_all_negative_numbers(self):

        # given
        prices = [-8, -3, -6, -2, -5, -4]
        low = 0
        high = len(prices) - 1
        expected_result = (3, 3, -2)  # Максимальный элемент сам по себе: -2

        # when
        result = find_maximum_subarray(prices, low, high)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_all_positive_numbers(self):
        
        # given
        prices = [1, 2, 3, 4, 5]
        low = 0
        high = len(prices) - 1
        expected_result = (0, 4, 15)  # Весь массив с суммой 15

        # when
        result = find_maximum_subarray(prices, low, high)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
