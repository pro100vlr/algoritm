import unittest
from lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_linear_search1(self):
        
        # given
        sorted_arr = [1, 5, 8, 12, 13]
        target = 8
        expected_output = 2

        # then
        result = binary_search(sorted_arr, target)

        # when
        self.assertEqual(result, expected_output)
        
    def test_should_find_target_in_middle(self):

        # given
        arr = [1, 2, 3, 4, 5, 6, 7]
        target = 4
        expected_result = 3  # Индекс элемента 4 в массиве

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_target_at_start(self):
        # given
        arr = [1, 2, 3, 4, 5]
        target = 1
        expected_result = 0  # Индекс элемента 1

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_target_at_end(self):

        # given
        arr = [1, 2, 3, 4, 5]
        target = 5
        expected_result = 4  # Индекс элемента 5

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_minus_one_when_target_not_in_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        target = 10
        expected_result = -1  # Элемент не найден

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_single_element_array_target_found(self):

        # given
        arr = [42]
        target = 42
        expected_result = 0  # Единственный элемент найден

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_minus_one_with_single_element_array_target_not_found(self):
        # given
        arr = [42]
        target = 7
        expected_result = -1  # Элемент отсутствует в массиве

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_large_array(self):

        # given
        arr = list(range(1, 10001))  # Массив от 1 до 10,000
        target = 9999
        expected_result = 9998  # Индекс элемента 9999

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
   unittest.main()