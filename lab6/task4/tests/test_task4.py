import unittest
from lab6.task4.src.task4 import process_operations
from utils import measure

class Test(unittest.TestCase):
    def test_should_сheck_time_and_memory(self):
        
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

    def test_should_сheck_put_and_get(self):

        # given
        operations = [
            ["put", "a", "1"],
            ["put", "b", "2"],
            ["get", "a"],
            ["get", "b"],
            ["get", "c"]
        ]
        expected_result = ["1", "2", "<none>"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_сheck_prev_and_next(self):

        # given
        operations = [
            ["put", "a", "1"],
            ["put", "b", "2"],
            ["put", "c", "3"],
            ["prev", "b"],
            ["next", "b"],
            ["prev", "a"],
            ["next", "c"]
        ]
        expected_result = ["1", "3", "<none>", "<none>"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_сheck_delete(self):

        # given
        operations = [
            ["put", "a", "1"],
            ["put", "b", "2"],
            ["delete", "a"],
            ["get", "a"],
            ["prev", "b"],
            ["delete", "b"],
            ["get", "b"]
        ]
        expected_result = ["<none>", "<none>", "<none>"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_сheck_overwrite_value(self):
        # given
        operations = [
            ["put", "a", "1"],
            ["put", "a", "2"],
            ["get", "a"]
        ]
        expected_result = ["2"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_сheck_complex_case(self):

        # given
        operations = [
            ["put", "a", "1"],
            ["put", "b", "2"],
            ["put", "c", "3"],
            ["delete", "b"],
            ["get", "b"],
            ["prev", "c"],
            ["next", "a"],
            ["put", "d", "4"],
            ["next", "c"]
        ]
        expected_result = ["<none>", "1", "3", "4"]

        # when
        result = process_operations(operations)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
