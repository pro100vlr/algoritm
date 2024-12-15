import unittest
from lab2.task3.src.task3 import merge_sort_and_count
from utils import measure

class TestMergeSortAndCount(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        n = 10
        arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        temp_arr = [0] * n
        expected_output = 17
        expected_time = 2
        expected_memory = 256

        # then
        result = merge_sort_and_count(arr, temp_arr, 0, n - 1)
        time, memory = measure(merge_sort_and_count, arr, temp_arr, 0, n - 1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)


    def test_should_count_inversions_in_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        temp_arr = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        expected_inversions = 10  

        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [1, 2, 3, 4, 5])  

    def test_should_count_inversions_in_already_sorted_array(self):

        # given
        arr = [1, 2, 3, 4, 5]
        temp_arr = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        expected_inversions = 0  

        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [1, 2, 3, 4, 5])  

    def test_should_count_inversions_with_duplicates(self):

        # given
        arr = [3, 3, 2, 1]
        temp_arr = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        expected_inversions = 5  

        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [1, 2, 3, 3])  

    def test_should_count_inversions_in_single_element_array(self):

        # given
        arr = [42]
        temp_arr = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        expected_inversions = 0  

        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [42])  

    def test_should_count_inversions_in_empty_array(self):

        # given
        arr = []
        temp_arr = []
        left = 0
        right = len(arr) - 1
        expected_inversions = 0 

        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [])  

    def test_should_count_inversions_in_mixed_array(self):

        # given
        arr = [8, 4, 2, 1]
        temp_arr = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        expected_inversions = 6  
        # when
        actual_inversions = merge_sort_and_count(arr, temp_arr, left, right)

        # then
        self.assertEqual(actual_inversions, expected_inversions)
        self.assertEqual(arr, [1, 2, 4, 8])  

if __name__ == "__main__":
    unittest.main()