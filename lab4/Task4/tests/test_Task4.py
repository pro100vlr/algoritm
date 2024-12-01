import unittest
from Task4.src.Task4 import check_brackets
class Test(unittest.TestCase):
    def test_check_brackets1(self):
        # given
        sequence = '[]'
        expected_output = 'Success'

        # then
        result = check_brackets(sequence)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_check_brackets2(self):
        # given
        sequence = '{'
        expected_output = 1

        # then
        result = check_brackets(sequence)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_check_brackets3(self):
        # given
        sequence = 'foo(bar);'
        expected_output = 'Success'

        # then
        result = check_brackets(sequence)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
    unittest.main()