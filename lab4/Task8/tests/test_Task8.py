import unittest
from Task8.src.Task8 import evaluate_postfix
class Test(unittest.TestCase):
    def test_evaluate_postfix(self):
        # given
        expression = ['8', '9', '+', '1', '7', '-', '*']
        expected_output = -102

        # then
        result = evaluate_postfix(expression)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()