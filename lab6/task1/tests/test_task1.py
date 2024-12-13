import unittest
from lab6.task1.src.task1 import process_operations
from utils import measure

class Test(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        operations = [['A', '2'], ['A', '5'], ['A', '3'], ['?', '2'], ['?', '4'], ['A', '2'], ['D', '2'], ['?', '2']]
        expected_output = ['Y', 'N', 'N']
        expected_time = 2
        expected_memory = 256

        # then
        expected_result = process_operations(operations)
        time, memory = measure(process_operations, operations)

        # when
        self.assertEqual(expected_result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)
    
    def test_should_сheck_add_and_check(self):
        
        # given
        operations = [
            ("A", 1),
            ("A", 2),
            ("?", 1),
            ("?", 2),
            ("?", 3)
        ]

        # then
        expected_result = ["Y", "Y", "N"]

        # when
        self.assertEqual(process_operations(operations), expected_result)

    def test_should_сheck_remove_and_check(self):

        # given
        operations = [
            ("A", 1),
            ("A", 2),
            ("D", 1),
            ("?", 1),
            ("?", 2)
        ]

        # then
        expected_result = ["N", "Y"]

        # when
        self.assertEqual(process_operations(operations), expected_result)

    def test_should_сheck_add_duplicate(self):

        # given
        operations = [
            ("A", 1),
            ("A", 1),
            ("?", 1)
        ]

        # then
        expected_result = ["Y"]

        # when
        self.assertEqual(process_operations(operations), expected_result)

    def test_should_сheck_remove_nonexistent(self):

        # given
        operations = [
            ("D", 1),
            ("?", 1)
        ]

        # then
        expected_result = ["N"]

        # when
        self.assertEqual(process_operations(operations), expected_result)

if __name__ == "__main__":
    unittest.main()