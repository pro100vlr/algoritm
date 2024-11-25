import unittest
from Task2.src.Task2 import anti_quick_sort
class Test(unittest.TestCase):
    def test_case_1(self):
        n = 3
        expected_output = [1, 3, 2]
        self.assertEqual(anti_quick_sort(n), expected_output)


if __name__ == "__main__":
    unittest.main()