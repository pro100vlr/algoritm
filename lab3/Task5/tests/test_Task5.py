import unittest
from lab3.task5.src.task5 import h_index 
from utils import measure

class TestHIndext(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        citations = [2, 1, 3]
        expected_output = 2
        expected_time = 2
        expected_memory = 256
        
        # then
        result =h_index(citations)
        time, memory = measure(h_index, citations)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_return_correct_h_index_for_typical_case(self):

        # given
        citations = [6, 5, 3, 1, 0]
        expected_result = 3

        # when
        result = h_index(citations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_zero_for_all_zero_citations(self):

        # given
        citations = [0, 0, 0, 0]
        expected_result = 0

        # when
        result = h_index(citations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_h_index_for_all_equal_citations(self):

        # given
        citations = [4, 4, 4, 4]
        expected_result = 4

        # when
        result = h_index(citations)

        # then
        self.assertEqual(result, expected_result)


    def test_should_return_h_index_for_unsorted_citations(self):

        # given
        citations = [3, 0, 6, 1, 5]
        expected_result = 3

        # when
        result = h_index(citations)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_h_index_for_empty_list(self):

        # given
        citations = []
        expected_result = 0

        # when
        result = h_index(citations)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()