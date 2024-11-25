import unittest
from Task8.src.Task8 import k_closest_points
class Test(unittest.TestCase):
    def test_case_1(self):
        points = [(1, 3), (-2, 2)]
        K = 1
        expected_output = [(-2, 2)]
        self.assertEqual(k_closest_points(points, K), expected_output)
    def test_case_2(self):
        points = [(3, 3), (5, -1), (-2, 4)]
        K = 2
        expected_output = [(3, 3), (-2, 4)]
        self.assertEqual(k_closest_points(points, K), expected_output)

if __name__ == "__main__":
    unittest.main()