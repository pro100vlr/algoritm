import unittest
from Task2.src.Task2 import anti_quick_sort
class Test(unittest.TestCase):
    def test_anti_quick_sort(self):
        # given
        n = 3
        expected_output = [1, 3, 2]

        # then
        result = anti_quick_sort(n)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()