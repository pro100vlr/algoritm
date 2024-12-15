import unittest
from lab2.task5.src.task5 import find_majority_element
from utils import measure

class TestFindMajorityElement(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        n = 5
        arr = [2, 3, 9, 2, 2]
        expected_output = 2
        expected_time = 2
        expected_memory = 256
        
        # then
        result =find_majority_element(arr, n)
        time, memory = measure(find_majority_element, arr, n)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_find_majority_element(self):
        
        # given
        arr = [3, 3, 4, 2, 3, 3, 3]
        n = len(arr)
        expected_result = 3  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_none_when_no_majority_element(self):
        
        # given
        arr = [1, 2, 3, 4, 5, 6, 7]
        n = len(arr)
        expected_result = None  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_array_with_single_element(self):
        
        # given
        arr = [42]
        n = len(arr)
        expected_result = 42  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_array_with_all_elements_same(self):
       
        # given
        arr = [7, 7, 7, 7, 7]
        n = len(arr)
        expected_result = 7  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_none_when_array_is_empty(self):
        
        # given
        arr = []
        n = len(arr)
        expected_result = None  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_array_with_majority_element_at_end(self):
        # given
        arr = [1, 2, 1, 2, 1, 1]
        n = len(arr)
        expected_result = 1  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_array_with_majority_element_at_start(self):
        
        # given
        arr = [10, 10, 10, 2, 3, 10]
        n = len(arr)
        expected_result = 10  

        # when
        result = find_majority_element(arr, n)

        # then
        self.assertEqual(result, expected_result)
   
if __name__ == "__main__":
    unittest.main()
