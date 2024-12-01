import unittest
from Task7.src.Task7 import heap_sort
class Test(unittest.TestCase):
    def test_build_max_heap(self):
        # given
        array = [8, 9, 2, 10, 15]
        expected_output = [2, 8, 9, 10, 15]

        # then
        result = heap_sort(array)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()