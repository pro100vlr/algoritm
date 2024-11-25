import unittest
from Task8.src.Task8 import evaluate_postfix
class Test(unittest.TestCase):
    def test_case_1(self):
        expression = ['8', '9', '+', '1', '7', '-', '*']
        expected_output = -102
        self.assertEqual(evaluate_postfix(expression), expected_output)


if __name__ == "__main__":
    unittest.main()