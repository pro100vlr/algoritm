import unittest
from lab7.task5.src.task5 import longest_common_subsequence
from utils import measure

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_should_handle_single_common_subsequence(self):

        # given
        a = [1, 2, 3]
        b = [2, 1, 3]
        c = [1, 3, 5]
        n = len(a)
        m = len(b)
        l = len(c)
        expected_result = 2  # Общая подпоследовательность: (1, 3)
        expected_time = 1

        # then
        result = longest_common_subsequence(a, b, c, n, m, l)
        time, _ = measure(longest_common_subsequence, a, b, c, n, m, l)

        # when
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time, expected_time)

    def test_should_handle_multiple_common_subsequences(self):

        # given
        a = [8, 3, 2, 1, 7]
        b = [8, 2, 1, 3, 8, 1, 0, 7]
        c = [6, 8, 1, 3, 4, 7]
        n = len(a)
        m = len(b)
        l = len(c)
        expected_result = 3  # Общие подпоследовательности: (8, 3, 7) и (8, 1, 7)

        # then
        result = longest_common_subsequence(a, b, c, n, m, l)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_no_common_elements(self):

        # given
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [7, 8, 9]
        n = len(a)
        m = len(b)
        l = len(c)
        expected_result = 0  # Общих элементов нет

        # then
        result = longest_common_subsequence(a, b, c, n, m, l)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_identical_sequences(self):

        # given
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        c = [1, 2, 3, 4, 5]
        n = len(a)
        m = len(b)
        l = len(c)
        expected_result = 5  # Полное совпадение

        # then
        result = longest_common_subsequence(a, b, c, n, m, l)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_single_character_sequences(self):
        
        # given
        a = [1]
        b = [1]
        c = [1]
        n = len(a)
        m = len(b)
        l = len(c)
        expected_result = 1  # Общий элемент: 1

        # then
        result = longest_common_subsequence(a, b, c, n, m, l)

        # when
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
