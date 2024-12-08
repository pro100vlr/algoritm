import unittest
from lab6.task7.src.task7 import count_beautiful_pairs
from utils import measure

class Test(unittest.TestCase):

    expected_time = 1
    expected_memory = 64
     
    def test_should_count_beautiful_one_pair_successful(self):
        # given
        n = 7
        k = 1
        s = 'abacaba'
        pairs = [('a', 'a')]
        expected_output = 6
   
        # then
        result = count_beautiful_pairs(n, k, s, pairs)
        time, memory = measure(count_beautiful_pairs, n, k, s, pairs)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_count_beautiful_three_pairs_successful(self):
        # given
        n = 7
        k = 3
        s = 'abacaba'
        pairs = [('a', 'b'), ('a', 'c'), ('b', 'b')]
        expected_output = 7

        # then
        result = count_beautiful_pairs(n, k, s, pairs)
        time, memory = measure(count_beautiful_pairs, n, k, s, pairs)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == "__main__":
    unittest.main()