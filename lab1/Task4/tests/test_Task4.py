import unittest
from Task4.src.Task4 import linear_search
class Test(unittest.TestCase):
    def test_case_1(self):
        arr = [3, 5, 7, 8, 9, 5, 6, 3, 4, 5, 10, 7, 3, 5]
        target = 5
        expected_output = [2, 6, 10, 14]
        self.assertEqual(linear_search(arr, target), expected_output)


if __name__ == "__main__":
    unittest.main()