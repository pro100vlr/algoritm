import unittest
from lab6.task1.src.task1 import process_operations
from utils import measure

class Test(unittest.TestCase):
    def test_should_process_operations_successful(self):
        # given
        
        operations = [['A', '2'], ['A', '5'], ['A', '3'], ['?', '2'], ['?', '4'], ['A', '2'], ['D', '2'], ['?', '2']]
        expected_output = ['Y', 'N', 'N']
        expected_time = 2
        expected_memory = 256

        # then
        result = process_operations(operations)
        time, memory = measure(process_operations, operations)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

if __name__ == "__main__":
    unittest.main()