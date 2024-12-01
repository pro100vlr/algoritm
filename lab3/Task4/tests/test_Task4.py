import unittest
from Task4.src.Task4 import count_segments_containing_points
class Test(unittest.TestCase):
    def test_count_segments_containing_points1(self):
        # given
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected_output = [1, 0, 0]

        # then
        result = count_segments_containing_points(segments, points)

        # when
        self.assertEqual(result, expected_output)
        print('Success')
    def test_count_segments_containing_points2(self):
        # given
        segments = [(0, 5), (-3, 2), (7, 10)]
        points = [1, 6]
        expected_output = [2, 0]

        # then
        result = count_segments_containing_points(segments, points)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()