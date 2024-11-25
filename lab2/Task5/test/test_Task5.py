import unittest
from Task5.src.Task5 import find_majority_element


class Test(unittest.TestCase):
    def test_case_1(self):
        arr = [2, 3, 9, 2, 2]
        n = 5
        expected_output = 2
        self.assertEqual(find_majority_element(arr, n), expected_output)

    def test_case_2(self):
        arr = [1, 2, 3, 4]
        n = 4
        expected_output = None
        self.assertEqual(find_majority_element(arr, n), expected_output)


if __name__ == "__main__":
    unittest.main()
