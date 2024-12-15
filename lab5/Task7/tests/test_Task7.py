import unittest
from lab5.task7.src.task7 import heap_sort, max_heapify, build_max_heap

class TestHeapFunctions(unittest.TestCase):        
    def test_should_heapify_correctly(self):

        # given
        array = [4, 10, 3, 5, 1]
        n = len(array)
        i = 1
        expected_result = [4, 10, 3, 5, 1]  # Куча уже корректная после этой операции

        # when
        max_heapify(array, n, i)

        # then
        self.assertEqual(array, expected_result)

    def test_should_build_max_heap_correctly(self):

        # given
        array = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
        n = len(array)
        expected_result = [20, 18, 10, 12, 9, 9, 3, 5, 6, 8]

        # when
        build_max_heap(array, n)

        # then
        self.assertEqual(array, expected_result)

    def test_should_sort_correctly_using_heap_sort(self):

        # given
        array = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
        expected_result = [3, 5, 6, 8, 9, 9, 10, 12, 18, 20]

        # when
        result = heap_sort(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_empty_array(self):

        # given
        array = []
        expected_result = []

        # when
        result = heap_sort(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_single_element_array(self):

        # given
        array = [42]
        expected_result = [42]

        # when
        result = heap_sort(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()