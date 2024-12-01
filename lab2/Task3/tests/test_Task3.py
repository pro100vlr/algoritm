import unittest
from Task3.src.Task3 import merge_sort_and_count

class Test(unittest.TestCase):
    def test_merge_sort_and_count(self):
        # given
        arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        n = 10
        temp_arr = [0] * n
        expected_output = 17

        # then
        result = merge_sort_and_count(arr, temp_arr, 0, n - 1)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
   unittest.main()