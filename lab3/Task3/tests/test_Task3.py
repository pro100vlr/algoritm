import unittest
from lab3.task3.src.task3 import can_sort_with_k_swaps
from utils import measure

class Test(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        k = 2
        n = 3
        arr = [2, 1, 3]
        expected_output = 'НЕТ'
        expected_time = 2
        expected_memory = 256
        
        # then
        result =can_sort_with_k_swaps(n, k, arr)
        time, memory = measure(can_sort_with_k_swaps, n, k, arr)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_no_when_not_sortable(self):

        # given
        n = 6
        k = 2
        sizes = [3, 1, 4, 2, 6, 5]
        expected_result = "НЕТ"

        # when
        result = can_sort_with_k_swaps(n, k, sizes)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_yes_for_single_group(self):

        # given
        n = 4
        k = 1
        sizes = [4, 3, 2, 1]
        expected_result = "ДА"

        # when
        result = can_sort_with_k_swaps(n, k, sizes)

        # then
        self.assertEqual(result, expected_result)


    def test_should_handle_empty_array(self):

        # given
        n = 0
        k = 1
        sizes = []
        expected_result = "ДА"

        # when
        result = can_sort_with_k_swaps(n, k, sizes)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_no_for_large_unsortable_case(self):

        # given
        n = 8
        k = 3
        sizes = [8, 1, 2, 7, 3, 4, 6, 5]
        expected_result = "НЕТ"

        # when
        result = can_sort_with_k_swaps(n, k, sizes)

        # then
        self.assertEqual(result, expected_result)
    
if __name__ == "__main__":
    unittest.main()