import unittest
from Task4.src.Task4 import linear_search
class Test(unittest.TestCase):
    def test_linear_search(self):
        # given
        arr = [3, 5, 7, 8, 9, 5, 6, 3, 4, 5, 10, 7, 3, 5]
        target = 5
        expected_output = [2, 6, 10, 14]

        # then
        result = linear_search(arr, target)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()