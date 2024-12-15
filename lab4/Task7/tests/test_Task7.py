import unittest
from lab4.task7.src.task7 import sliding_window_maximum
from utils import measure

class TestSlidingWindowMaximum(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        arr = [2, 7, 3, 1, 5, 2, 6, 2]
        n = 8
        m = 4
        expected_output = [7, 7, 5, 6, 6]
        expected_time = 5
        expected_memory = 512

        # then
        result = sliding_window_maximum(arr, n, m)
        time, memory = measure(sliding_window_maximum, arr, n, m)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_correct_maximums(self):

        # given
        arr = [1, 3, -1, -3, 5, 3, 6, 7]
        n = len(arr)
        m = 3
        expected_result = [3, 3, 5, 5, 6, 7]

        # when
        result = sliding_window_maximum(arr, n, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_single_element_window(self):

        # given
        arr = [4, 2, 12, 1, 7]
        n = len(arr)
        m = 1
        expected_result = [4, 2, 12, 1, 7]

        # when
        result = sliding_window_maximum(arr, n, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_window_equal_to_array_size(self):
        # given
        arr = [2, 5, 1, 3]
        n = len(arr)
        m = 4
        expected_result = [5]

        # when
        result = sliding_window_maximum(arr, n, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_empty_for_empty_array(self):

        # given
        arr = []
        n = len(arr)
        m = 3
        expected_result = []

        # when
        result = sliding_window_maximum(arr, n, m)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_window_size(self):
        
        # given
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        m = 10
        expected_result = []

        # when
        result = sliding_window_maximum(arr, n, m)

        # then
        self.assertEqual(result, expected_result)
   
if __name__ == "__main__":
    unittest.main()
