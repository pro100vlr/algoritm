import unittest
from Task3.src.Task3 import can_sort_with_k_swaps
class Test(unittest.TestCase):
    def test_case_1(self):
        n = 3
        k = 2
        sizes=[2, 1, 3]
        expected_output = "НЕТ"
        self.assertEqual(can_sort_with_k_swaps(n, k, sizes), expected_output)
    def test_case_2(self):
        n = 5
        k = 3
        sizes=[1, 5, 3, 4, 1]
        expected_output = "ДА"
        self.assertEqual(can_sort_with_k_swaps(n, k, sizes), expected_output)

if __name__ == "__main__":
    unittest.main() 