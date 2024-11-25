import unittest
from Task4.src.Task4 import check_brackets
class Test(unittest.TestCase):
    def test_case_1(self):
        sequence = '[]'
        expected_output = 'Success'
        self.assertEqual(check_brackets(sequence), expected_output)
    def test_case_2(self):
        sequence = '{'
        expected_output = 1
        self.assertEqual(check_brackets(sequence), expected_output)
    def test_case_3(self):
        sequence = 'foo(bar);'
        expected_output = 'Success'
        self.assertEqual(check_brackets(sequence), expected_output)

if __name__ == "__main__":
    unittest.main()