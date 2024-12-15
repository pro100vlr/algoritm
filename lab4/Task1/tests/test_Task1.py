import unittest
from lab4.task1.src.task1 import process_stack_commands
from utils import measure

class TestProcessStackCommands(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        commands = ['+ 1', '+ 10','-','+ 2', '+ 1234', '-']
        expected_output = [10, 1234]
        expected_time = 2
        expected_memory = 256

        # then
        result = process_stack_commands(commands)
        time, memory = measure(process_stack_commands, commands)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_add_and_remove_elements(self):

        # given
        commands = ['+ 5', '+ 10', '-']
        expected_result = [10]

        # when
        result = process_stack_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_removals(self):

        # given
        commands = ['+ 5', '+ 10', '+ 20', '-', '-']
        expected_result = [20, 10]

        # when
        result = process_stack_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_empty_stack_removal(self):

        # given
        commands = ['-', '-']
        expected_result = []

        # when
        result = process_stack_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_no_commands(self):

        # given
        commands = []
        expected_result = []

        # when
        result = process_stack_commands(commands)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_only_additions(self):
        
        # given
        commands = ['+ 1', '+ 2', '+ 3']
        expected_result = []

        # when
        result = process_stack_commands(commands)

        # then
        self.assertEqual(result, expected_result)
    
if __name__ == "__main__":
    unittest.main()



    
    