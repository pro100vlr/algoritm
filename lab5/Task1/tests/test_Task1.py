import unittest
from Task1.src.Task1 import is_heap
class Test(unittest.TestCase):
    def test_is_heap1(self):
        # given
        array = [1, 0, 1, 2, 0]
        n = 5
        expected_output = 'NO'

        # then
        result = is_heap(n, array)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_is_heap2(self):
        # given
        array = [1, 3, 2, 5, 4]
        n = 5
        expected_output = 'YES'

        # then
        result = is_heap(n, array)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()