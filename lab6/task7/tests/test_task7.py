import unittest
from lab6.task7.src.task7 import count_beautiful_pairs
from utils import measure

class TestBeautifulPairs(unittest.TestCase):
     
    def test_should_сheck_time_and_memory(self):

        # given
        n = 7
        k = 1
        s = 'abacaba'
        pairs = [('a', 'a')]
        expected_output = 6
        expected_time = 1
        expected_memory = 64
   
        # then
        result = count_beautiful_pairs(n, k, s, pairs)
        time, memory = measure(count_beautiful_pairs, n, k, s, pairs)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_count_beautiful_pairs_correctly(self):

        # given
        n = 5
        k = 2
        s = "abcba"
        pairs = [("a", "b"), ("b", "c")]
        expected_result = 3

        # when
        result = count_beautiful_pairs(n, k, s, pairs)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_zero_if_no_pairs_are_beautiful(self):

        # given
        n = 4
        k = 1
        s = "abcd"
        pairs = [("x", "y")]
        expected_result = 0

        # when
        result = count_beautiful_pairs(n, k, s, pairs)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_repeated_characters(self):

        # given
        n = 6
        k = 2
        s = "aaaaaa"
        pairs = [("a", "a")]
        expected_result = 15

        # when
        result = count_beautiful_pairs(n, k, s, pairs)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_input(self):

        # given
        n = 100000
        k = 1
        s = "a" * n
        pairs = [("a", "a")]
        expected_result = (n * (n - 1)) // 2

        # when
        result = count_beautiful_pairs(n, k, s, pairs)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_beautiful_pairs(self):

        # given
        n = 7
        k = 3
        s = "abcacba"
        pairs = [("a", "b"), ("b", "c"), ("c", "a")]
        expected_result = 8

        # when
        result = count_beautiful_pairs(n, k, s, pairs)

        # then
        self.assertEqual(result, expected_result)
        

if __name__ == "__main__":
    unittest.main()