import unittest
from Task8.src.Task8 import k_closest_points
class Test(unittest.TestCase):
    def test_k_closest_points1(self):
        # given
        points = [(1, 3), (-2, 2)]
        K = 1
        expected_output = [(-2, 2)]

        # then
        result = k_closest_points(points, K)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_k_closest_points2(self):
        # given
        points = [(3, 3), (5, -1), (-2, 4)]
        K = 2
        expected_output = [(3, 3), (-2, 4)]

        # then
        result = k_closest_points(points, K)

        # when
        self.assertEqual(result, expected_output)
        print('Success')

if __name__ == "__main__":
    unittest.main()