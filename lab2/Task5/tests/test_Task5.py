import unittest
from Task5.src.Task5 import find_majority_element


class Test(unittest.TestCase):
    def test_find_majority_element1(self):
        # given
        arr = [2, 3, 9, 2, 2]
        n = 5
        expected_output = 2

        # then
        result = find_majority_element(arr, n)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_find_majority_element2(self):
        # given
        arr = [1, 2, 3, 4]
        n = 4
        expected_output = None

        # then
        result = find_majority_element(arr, n)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()
