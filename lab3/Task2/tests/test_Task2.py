import unittest
from lab3.task2.src.task2 import anti_quick_sort
from utils import measure

class TestAntiQuickSort(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        n = 3
        expected_output = [1, 3, 2]
        expected_time = 2
        expected_memory = 256

        # then
        result = anti_quick_sort(n)
        time, memory = measure(anti_quick_sort, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_generate_correct_sequence_for_small_n(self):

        # given
        n = 5
        expected_result = [1, 4, 5, 3, 2]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_n_equal_to_one(self):

        # given
        n = 1
        expected_result = [1]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_n_equal_to_two(self):

        # given
        n = 2
        expected_result = [1, 2]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

 
    def test_should_generate_correct_sequence_for_large_n(self):

        # given
        n = 10
        expected_result = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_empty_list_for_n_equal_to_zero(self):
        
        # given
        n = 0
        expected_result = []

        # when
        result = anti_quick_sort(n)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()