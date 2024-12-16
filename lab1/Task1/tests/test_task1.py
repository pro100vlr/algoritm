import unittest
from lab1.task1.src.task1 import insertion_sort
from utils import read_file_data, measure

class TestInsertionSort(unittest.TestCase):
    expected_time = 2
    expected_memory = 256

    @classmethod
    def setUpClass(cls):
        print("InsertionSort")

    def test_should_sort_array_case_average(self):

        # given
        data = read_file_data('lab1/task1/tests/input_average.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)

        # then
        result =insertion_sort(arr, n)
        time, memory = measure(insertion_sort, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_sort_array_case_best(self):

        # given
        data = read_file_data('lab1/task1/tests/input_best.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)

        # then
        result = insertion_sort(arr, n)
        time, memory = measure(insertion_sort, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_sort_array_case_worst(self):

        # given
        data = read_file_data('lab1/task1/tests/input_worst.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)

        # then
        result = insertion_sort(arr, n)
        time, memory = measure(insertion_sort, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_handle_empty_array(self):

        # given
        arr = []
        n = len(arr)
        expected_output = []

        # then
        result = insertion_sort(arr, n)
        time, memory = measure(insertion_sort, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_handle_single_element_array(self):
        
        # given
        arr = [42]
        n = len(arr)
        expected_output = [42]

        # then
        result = insertion_sort(arr, n)
        time, memory = measure(insertion_sort, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == "__main__":
    unittest.main()

