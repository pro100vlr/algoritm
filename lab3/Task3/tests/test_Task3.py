import unittest
from Task3.src.Task3 import can_sort_with_k_swaps
class Test(unittest.TestCase):
    def test_can_sort_with_k_swaps1(self):
        # given
        n = 3
        k = 2
        sizes=[2, 1, 3]
        expected_output = "НЕТ"

        # then
        result = can_sort_with_k_swaps(n, k, sizes)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_can_sort_with_k_swaps2(self):
        # given
        n = 5
        k = 3
        sizes=[1, 5, 3, 4, 1]
        expected_output = "ДА"

        # then 
        result = can_sort_with_k_swaps(n, k, sizes)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
    unittest.main() 