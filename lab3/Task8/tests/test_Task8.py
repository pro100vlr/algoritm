import unittest
from lab3.task8.src.task8 import k_closest_points

class TestKClosestPoints(unittest.TestCase):
    def test_should_check_time_and_memory(self):

        # given
        points = [(1, 3), (-2, 2)]
        K = 1
        expected_output = [(-2, 2)]

        # then
        result = k_closest_points(points, K)

        # when
        self.assertEqual(result, expected_output)
        
    def test_should_return_closest_points_for_typical_case(self):

        # given
        points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
        K = 2
        expected_result = [(0, 1), (-2, 2)]

        # when
        result = k_closest_points(points, K)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_single_point_case(self):

        # given
        points = [(1, 2)]
        K = 1
        expected_result = [(1, 2)]

        # when
        result = k_closest_points(points, K)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_all_points_when_k_equals_length(self):

        # given
        points = [(1, 3), (-2, 2)]
        K = 2
        expected_result = [(-2, 2), (1, 3)]

        # when
        result = k_closest_points(points, K)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_empty_list_for_k_zero(self):

        # given
        points = [(1, 3), (-2, 2), (5, 8)]
        K = 0
        expected_result = []

        # when
        result = k_closest_points(points, K)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_k_with_duplicates(self):
        
        # given
        points = [(1, 1), (1, 1), (2, 2), (2, 2)]
        K = 3
        expected_result = [(1, 1), (1, 1), (2, 2)]

        # when
        result = k_closest_points(points, K)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()