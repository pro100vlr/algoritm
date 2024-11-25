import unittest
from Task1.src.Task1 import process_stack_commands
class Test(unittest.TestCase):
    def test_case_1(self):
        commands = ['+ 1', '+ 10','-','+ 2', '+ 1234', '-']
        expected_output = [10, 1234]
        self.assertEqual(process_stack_commands(commands), expected_output)


if __name__ == "__main__":
    unittest.main()