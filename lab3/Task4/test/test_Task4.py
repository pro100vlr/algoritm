import unittest
from Task4.src.Task4 import count_segments_containing_points
class Test(unittest.TestCase):
    def test_case_1(self):
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected_output = [1, 0, 0]
        self.assertEqual(count_segments_containing_points(segments, points), expected_output)
    def test_case_2(self):
        segments = [(0, 5), (-3, 2), (7, 10)]
        points = [1, 6]
        expected_output = [2, 0]
        self.assertEqual(count_segments_containing_points(segments, points), expected_output)


if __name__ == "__main__":
    unittest.main()