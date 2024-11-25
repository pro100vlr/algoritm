import unittest
from Task2.src.Task2 import insertion_sort_with_position_tracking

class Test(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        n = 10
        expected_output = ([1, 2, 2, 2, 3, 5, 5, 6, 9, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(insertion_sort_with_position_tracking(arr, n), expected_output)


if __name__ == "__main__":
    unittest.main()