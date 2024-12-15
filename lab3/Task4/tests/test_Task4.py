import unittest
from lab3.task4.src.task4 import count_segments_containing_points

class TestCountSegmentsContainingPoints(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected_output = [1, 0, 0]

        # then
        result = count_segments_containing_points(segments, points)

        # when
        self.assertEqual(result, expected_output)

    def test_should_count_correctly_for_simple_case(self):

        # given
        segments = [(1, 4), (2, 6), (3, 5)]
        points = [2, 3, 7]
        expected_result = [2, 3, 0]

        # when
        result = count_segments_containing_points(segments, points)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_zeros_for_points_outside_segments(self):

        # given
        segments = [(1, 2), (3, 4), (5, 6)]
        points = [0, 7]
        expected_result = [0, 0]

        # when
        result = count_segments_containing_points(segments, points)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_empty_segments(self):

        # given
        segments = []
        points = [1, 2, 3]
        expected_result = [0, 0, 0]

        # when
        result = count_segments_containing_points(segments, points)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_overlapping_segments(self):
        # given
        segments = [(1, 10), (5, 15), (10, 20)]
        points = [10, 15]
        expected_result = [3, 2]

        # when
        result = count_segments_containing_points(segments, points)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_single_point_and_segment(self):
        # given
        segments = [(1, 5)]
        points = [3]
        expected_result = [1]

        # when
        result = count_segments_containing_points(segments, points)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()