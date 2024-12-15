import unittest
from lab7.task4.src.task4 import longest_common_subsequence
from utils import measure

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_should_handle_single_common_element(self):

        # given
        A = [2, 7, 5]
        B = [2, 8]
        n = len(A)
        m = len(B)
        expected_result = 1  # Общий элемент: 2
        expected_time = 1

        # then
        result = longest_common_subsequence(A, B, n, m)
        time, _ = measure(longest_common_subsequence, A, B, n, m)

        # when
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time, expected_time)

    def test_should_handle_no_common_elements(self):

        # given
        A = [1, 2, 3]
        B = [4, 5, 6]
        n = len(A)
        m = len(B)
        expected_result = 0  # Нет общих элементов

        # then
        result = longest_common_subsequence(A, B, n, m)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_common_subsequences(self):

        # given
        A = [1, 2, 3, 4]
        B = [2, 1, 4, 3]
        n = len(A)
        m = len(B)
        expected_result = 2  # Общие подпоследовательности: (2, 4) и (1, 3)

        # then
        result = longest_common_subsequence(A, B, n, m)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_identical_sequences(self):

        # given
        A = [1, 2, 3, 4]
        B = [1, 2, 3, 4]
        n = len(A)
        m = len(B)
        expected_result = 4  # Полное совпадение

        # then
        result = longest_common_subsequence(A, B, n, m)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_single_element_sequences(self):
        
        # given
        A = [3]
        B = [3]
        n = len(A)
        m = len(B)
        expected_result = 1  # Общий элемент: 3

        # then
        result = longest_common_subsequence(A, B, n, m)

        # when
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()