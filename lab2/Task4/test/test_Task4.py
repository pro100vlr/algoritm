import unittest
from Task4.src.Task4 import binary_search

class Test(unittest.TestCase):
    def test_case_1(self):
        sorted_arr = [1, 5, 8, 12, 13]
        target = 8
        expected_output = 2
        self.assertEqual(binary_search(sorted_arr, target), expected_output)
    def test_case_2(self):
        sorted_arr = [1, 5, 8, 12, 13]
        target = 1
        expected_output = 0
        self.assertEqual(binary_search(sorted_arr, target), expected_output)

if __name__ == "__main__":
   unittest.main()