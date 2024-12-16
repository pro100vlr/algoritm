import unittest
from lab3.task1.src.task1 import quick_sort, randomized_quick_sort, randomized_quick_sort_c_partition
from utils import read_file_data, measure

class TestQuickSort(unittest.TestCase):
    expected_time = 2
    expected_memory = 256

    @classmethod
    def setUpClass(cls):
        print("QuickSort")

    def test_should_sort_array_case_average(self):
        
        # given  
        data = read_file_data('lab3/task1/tests/input_average.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)
        
        # then
        result = quick_sort(arr, 0, n-1)
        time, memory = measure(quick_sort, arr, 0, n-1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_sort_array_case_best(self):

        # given
        data = read_file_data('lab3/task1/tests/input_best.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)
       
        # then
        result = quick_sort(arr, 0, n-1)
        time, memory = measure(quick_sort, arr, 0, n-1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_sort_array_case_worst(self):

        # given
        data = read_file_data('lab3/task1/tests/input_worst.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)

        # then
        result = quick_sort(arr, 0, n-1)
        time, memory = measure(quick_sort, arr, 0, n-1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

class TestRandomizedQuickSort(unittest.TestCase):
    expected_time = 2
    expected_memory = 256

    @classmethod
    def setUpClass(cls):
        print("RandomizedQuickSort")

    def test_should_sort_array_case_average(self):
        
        # given
        data = read_file_data('lab1/task1/tests/input_average.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)
        
        # then
        result = randomized_quick_sort(arr, 0, n - 1)
        time, memory = measure(randomized_quick_sort, arr, 0, n-1)

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
        result = randomized_quick_sort(arr, 0, n-1)
        time, memory = measure(randomized_quick_sort, arr, 0, n-1)

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
        result = randomized_quick_sort(arr, 0, n-1)
        time, memory = measure(randomized_quick_sort, arr, 0, n-1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

class TestRandomizedQuickSortCPartition(unittest.TestCase):
    expected_time = 2
    expected_memory = 256

    @classmethod
    def setUpClass(cls):
        print("RandomizedQuickSortCPartition")

    def test_should_sort_array_case_average(self):
        
        # given
        data = read_file_data('lab1/task1/tests/input_average.txt')
        n = data[0]
        arr = data[1]
        expected_output = sorted(arr)
        
        # then
        result = randomized_quick_sort_c_partition(arr, 0, n - 1)
        time, memory = measure(randomized_quick_sort_c_partition, arr, 0, n-1)

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
        result =randomized_quick_sort_c_partition(arr, 0, n-1)
        time, memory = measure(randomized_quick_sort_c_partition, arr, 0, n-1)

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
        result = randomized_quick_sort_c_partition(arr, 0, n-1)
        time, memory = measure(randomized_quick_sort_c_partition, arr, 0, n-1)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == "__main__":
    unittest.main()

