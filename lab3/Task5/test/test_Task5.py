import unittest
from Task5.src.Task5 import h_index
class Test(unittest.TestCase):
    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        expected_output = 3
        self.assertEqual(h_index(citations), expected_output)

    def test_case_2(self):
        citations = [1, 3, 1]
        expected_output = 1
        self.assertEqual(h_index(citations), expected_output)

if __name__ == "__main__":
    unittest.main()