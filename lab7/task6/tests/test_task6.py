import unittest
from utils import measure
from lab7.task6.src.task6 import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_should_handle_general_case(self):

        """Проверяет общий случай."""
        # given
        arr = [3, 29, 5, 5, 28, 6]
        n = len(arr)
        expected_length = 3
        expected_sequence = [3, 5, 28]
        expected_time = 2
        expected_memory = 256

        # then
        length, sequence = longest_increasing_subsequence(arr, n)
        time, memory = measure(longest_increasing_subsequence, arr, n)

        # when
        self.assertEqual(length, expected_length)
        self.assertEqual(sequence, expected_sequence)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_handle_single_element(self):

        """Проверяет случай с одним элементом."""
        # given
        arr = [10]
        n = len(arr)
        expected_length = 1
        expected_sequence = [10]

        # then
        length, sequence = longest_increasing_subsequence(arr, n)

        # when
        self.assertEqual(length, expected_length)
        self.assertEqual(sequence, expected_sequence)

    def test_should_handle_decreasing_sequence(self):

        """Проверяет строго убывающую последовательность."""
        # given
        arr = [9, 8, 7, 6, 5]
        n = len(arr)
        expected_length = 1
        expected_sequence = [9]  # Любой из элементов

        # then
        length, sequence = longest_increasing_subsequence(arr, n)

        # when
        self.assertEqual(length, expected_length)
        self.assertIn(sequence, [[x] for x in expected_sequence])

    def test_should_handle_all_increasing_sequence(self):

        """Проверяет строго возрастающую последовательность."""
        # given
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        expected_length = 5
        expected_sequence = [1, 2, 3, 4, 5]

        # then
        length, sequence = longest_increasing_subsequence(arr, n)

        # when
        self.assertEqual(length, expected_length)
        self.assertEqual(sequence, expected_sequence)

    def test_should_handle_repeated_elements(self):

        """Проверяет последовательность с повторяющимися элементами."""
        # given
        arr = [3, 3, 3, 3]
        n = len(arr)
        expected_length = 1
        expected_sequence = [3]  # Любой из элементов

        # then
        length, sequence = longest_increasing_subsequence(arr, n)

        # when
        self.assertEqual(length, expected_length)
        self.assertIn(sequence, [[x] for x in expected_sequence])

if __name__ == "__main__":
    unittest.main()
