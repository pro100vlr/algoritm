import unittest
from Task6.src.Task6 import process_commands
class Test(unittest.TestCase):
    def test_process_commands(self):
        # given
        commands = ['+ 1', '?','+ 10', '?', '-', '?', '-']
        expected_output = ['1', '1', '10']

        # then
        result = process_commands(commands)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()