import unittest
from lab4.task4.src.task4 import check_brackets
from utils import measure

class TestCheckBrackets(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        sequence = '[]'
        expected_output = 'Success'
        expected_time = 5
        expected_memory = 256
        
        # then
        result = check_brackets(sequence)
        time, memory = measure(check_brackets, sequence)
        
        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_success_for_correct_brackets(self):
        
        # given
        sequence = "()[]{}"
        expected_result = "Success"

        # when
        result = check_brackets(sequence)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_position_for_unmatched_closing_bracket(self):

        # given
        sequence = "([)]"
        expected_result = 3

        # when
        result = check_brackets(sequence)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_position_for_extra_closing_bracket(self):

        # given
        sequence = "()[]}"  # Лишняя закрывающая скобка
        expected_result = 5

        # when
        result = check_brackets(sequence)

        # then
        self.assertEqual(result, expected_result)

     
    def test_should_return_position_for_unmatched_opening_bracket(self):

        # given
        sequence = "({["
        expected_result = 1

        # when
        result = check_brackets(sequence)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_position_for_nested_incorrect_brackets(self):

        # given
        sequence = "{[}(]"
        expected_result = 3

        # when
        result = check_brackets(sequence)

        # then
        self.assertEqual(result, expected_result)

    
if __name__ == "__main__":
    unittest.main()