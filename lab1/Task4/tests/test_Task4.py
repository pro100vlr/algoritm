import unittest
from lab1.task4.src.task4 import linear_search

class TestLinearSearch(unittest.TestCase):    
    def test_should_return_single_index_when_target_found_once(self):
        
        # given
        arr = [5, 3, 7, 1, 4]
        target = 7
        expected_result = "3"  # Элемент найден на 3-й позиции (счёт с 1)

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_multiple_indices_when_target_found_multiple_times(self):
        
        # given
        arr = [2, 4, 6, 4, 4, 8]
        target = 4
        expected_result = "3\n2, 4, 5"  # Найден 3 раза на позициях 2, 4, 5

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_minus_one_when_target_not_found(self):
        
        # given
        arr = [1, 2, 3, 4, 5]
        target = 10
        expected_result = "-1"  # Элемент отсутствует

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_empty_array(self):
       
        # given
        arr = []
        target = 5
        expected_result = "-1"  # В пустом массиве ничего не найдётся

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_index_with_single_element_array(self):
        
        # given
        arr = [42]
        target = 42
        expected_result = "1"  # Единственный элемент найден на позиции 1

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_minus_one_with_single_element_array_not_found(self):
        
        # given
        arr = [42]
        target = 7
        expected_result = "-1"  # Элемент не найден

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_input_with_multiple_occurrences(self):
        
        # given
        arr = [1] * 1000  # 1000 элементов, все равны 1
        target = 1
        indices = ', '.join(map(str, range(1, 1001)))  # Индексы с 1 до 1000
        expected_result = f"1000\n{indices}"  # 1000 вхождений

        # when
        result = linear_search(arr, target)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()