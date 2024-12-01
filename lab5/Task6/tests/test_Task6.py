import unittest
from Task6.src.Task6 import process_operations
class Test(unittest.TestCase):
    def test_priority_queue(self):
        # given
        operations = [["A", "3"], ["A", "4"], ["A", "2"], ["X"], ["D", "2", "1"], ["X"], ["X"], ["X"]]
        expected_output = ['2', '1', '3', '*']

        # then
        result = process_operations(operations)
        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()