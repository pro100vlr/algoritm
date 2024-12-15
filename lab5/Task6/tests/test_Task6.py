import unittest
from lab5.task6.src.task6 import process_operations
from utils import measure

class TestProcessOperations(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        operations = [["A", "3"], ["A", "4"], ["A", "2"], ["X"], ["D", "2", "1"], ["X"], ["X"], ["X"]]
        expected_output = ['2', '1', '3', '*']
        expected_time = 2
        expected_memory = 256

        # then
        result = process_operations(operations)
        time, memory = measure(process_operations, operations)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)
    
    def test_should_add_and_extract_minimum(self):

        # given
        operations = [["A", "5"], ["A", "3"], ["X"], ["X"], ["X"]]
        expected_result = ["3", "5", "*"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_decrease_key_and_extract_minimum(self):

        # given
        operations = [["A", "5"], ["A", "3"], ["D", "1", "1"], ["X"], ["X"]]
        expected_result = ["1", "3"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_empty_heap_extraction(self):

        # given
        operations = [["X"], ["X"]]
        expected_result = ["*", "*"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    
    def test_should_handle_multiple_decrease_operations(self):

        # given
        operations = [["A", "10"], ["A", "20"], ["D", "1", "15"], ["D", "2", "5"], ["X"], ["X"]]
        expected_result = ["5", "15"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_no_operations(self):

        # given
        operations = []
        expected_result = []

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    
if __name__ == "__main__":
    unittest.main()



 