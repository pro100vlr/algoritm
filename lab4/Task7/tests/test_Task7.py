import unittest
from Task7.src.Task7 import sliding_window_maximum
class Test(unittest.TestCase):
    def test_case_1(self):
        arr = [2, 7, 3, 1, 5, 2, 6, 2]
        n = 8
        m = 4
        expected_output = [7, 7, 5, 6, 6]
        self.assertEqual(sliding_window_maximum(arr, n, m), expected_output)


if __name__ == "__main__":
    unittest.main()