import unittest
from lab5.task1.src.task1 import is_heap
from utils import measure

class TestIsHeap(unittest.TestCase):  
    def test_should_check_time_and_memory(self):
        
        # given
        array = [1, 0, 1, 2, 0]
        n = 5
        expected_output = 'NO'
        expected_time = 2
        expected_memory = 256
       
        # then
        result = is_heap(n, array)
        time, memory = measure(is_heap, n, array)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_yes_for_valid_heap(self):

        # given
        n = 5
        array = [1, 3, 5, 7, 9]
        expected_result = "YES"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_no_for_invalid_heap(self):

        # given
        n = 5
        array = [10, 3, 5, 7, 1]
        expected_result = "NO"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_yes_for_empty_heap(self):

        # given
        n = 0
        array = []
        expected_result = "YES"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)
    
    def test_should_return_yes_for_single_element_heap(self):

        # given
        n = 1
        array = [42]
        expected_result = "YES"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_no_for_left_child_violation(self):

        # given
        n = 3
        array = [10, 15, 5]
        expected_result = "NO"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_no_for_right_child_violation(self):

        # given
        n = 3
        array = [10, 5, 15]
        expected_result = "NO"

        # when
        result = is_heap(n, array)

        # then
        self.assertEqual(result, expected_result)
    
if __name__ == "__main__":
    unittest.main()

