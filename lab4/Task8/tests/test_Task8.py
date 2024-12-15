import unittest
from lab4.task8.src.task8 import evaluate_postfix
from utils import measure

class TestEvaluatePostfix(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        expression = ['8', '9', '+', '1', '7', '-', '*']
        expected_output = -102
        expected_time = 2
        expected_memory = 256

        # then
        result = evaluate_postfix(expression)
        time, memory = measure(evaluate_postfix, expression)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_evaluate_simple_expression(self):

        # given
        expression = ["2", "3", "+"]
        expected_result = 5

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_subtraction(self):

        # given
        expression = ["5", "3", "-"]
        expected_result = 2

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiplication(self):

        # given
        expression = ["4", "3", "*"]
        expected_result = 12

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_complex_expression(self):

        # given
        expression = ["2", "3", "+", "4", "*"]
        expected_result = 20

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_zero_for_single_zero(self):
        
        # given
        expression = ["0"]
        expected_result = 0

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()



   