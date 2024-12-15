import unittest
from lab4.task6.src.task6 import  process_commands
from utils import measure

class TestProcessCommands(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given 
        commands = ['+ 1', '?','+ 10', '?', '-', '?', '-']
        expected_output = ['1', '1', '10']
        expected_time = 2
        expected_memory = 256

        # then
        result =  process_commands(commands)
        time, memory = measure(process_commands, commands)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_minimum_after_additions(self):

        # given
        commands = ['+ 5', '+ 3', '+ 8', '?']
        expected_result = ['3']

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_update_minimum_after_removals(self):

        # given
        commands = ['+ 5', '+ 3', '+ 8', '-', '?']
        expected_result = ['3']

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_correct_minimum_after_mixed_operations(self):

        # given
        commands = ['+ 10', '+ 1', '+ 7', '-', '?', '+ 2', '?']
        expected_result = ['1', '1']

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_empty_queue_for_minimum_request(self):
        # given
        commands = ['?']
        expected_result = []

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_minimum_correctly_after_multiple_removals(self):
        # given
        commands = ['+ 10', '+ 5', '+ 3', '-', '-', '?']
        expected_result = ['3']

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()


   