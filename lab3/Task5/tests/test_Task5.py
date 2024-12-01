import unittest
from Task5.src.Task5 import h_index
class Test(unittest.TestCase):
    def test_h_index1(self):
        # given
        citations = [3, 0, 6, 1, 5]
        expected_output = 3

        # then
        result = h_index(citations)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_h_index2(self):
        # given
        citations = [1, 3, 1]
        expected_output = 1

        # then
        result = h_index(citations)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
    unittest.main()