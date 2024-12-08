import unittest
from lab6.task4.src.task4 import process_operations
from utils import measure

class Test(unittest.TestCase):
    def test_should_process_operations_successful(self):
        # given
        
        operations = [['put', 'zero', 'a'], ['put', 'one', 'b'], ['put', 'two', 'c'], ['put', 'three', 'd'], ['put', 'four', 'e'], ['get', 'two'], ['prev', 'two'], ['next', 'two'], ['delete', 'one'], ['delete', 'three'], ['get', 'two'], ['prev', 'two'], ['next', 'two'], ['next', 'four']]
        expected_output = ['c', 'b', 'd', 'c', 'a', 'e', '<none>']
        expected_time = 4
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