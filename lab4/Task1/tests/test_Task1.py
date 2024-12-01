import unittest
from Task1.src.Task1 import process_stack_commands
class Test(unittest.TestCase):
    def test_process_stack_commands(self):
        # given
        commands = ['+ 1', '+ 10','-','+ 2', '+ 1234', '-']
        expected_output = [10, 1234]

        # then
        result = process_stack_commands(commands)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()