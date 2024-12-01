import unittest
from Task4.src.Task4 import binary_search

class Test(unittest.TestCase):
    def test_linear_search1(self):
        # given
        sorted_arr = [1, 5, 8, 12, 13]
        target = 8
        expected_output = 2

        # then
        result = binary_search(sorted_arr, target)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_linear_search2(self):
        # given
        sorted_arr = [1, 5, 8, 12, 13]
        target = 1
        expected_output = 0

        # then
        result = binary_search(sorted_arr, target)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
   unittest.main()