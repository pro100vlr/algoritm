import unittest
from Task6.src.Task6 import process_commands
class Test(unittest.TestCase):
    def test_case_1(self):
        commands = ['+ 1', '?','+ 10', '?', '-', '?', '-']
        expected_output = ['1', '1', '10']
        self.assertEqual(process_commands(commands), expected_output)


if __name__ == "__main__":
    unittest.main()