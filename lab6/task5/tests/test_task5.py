import unittest
from lab6.task5.src.task5 import process_election_results
from utils import measure

class TestElectionResults(unittest.TestCase):

    def test_should_process_election_results_successful_two_candidates(self):
        # given
        
        data = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expected_output = ['McCain 16', 'Obama 17']
        expected_time = 2
        expected_memory = 64

        # then
        result = process_election_results(data)
        time, memory = measure(process_election_results, data)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_correctly_count_votes_for_single_candidate(self):

        # given
        data = [
            "Smith 10",
            "Smith 20",
            "Smith 30"
        ]
        expected_result = ["Smith 60"]

        # when
        result = process_election_results(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_candidates_lexicographically(self):

        # given
        data = [
            "Smith 10",
            "Adams 20",
            "Brown 30"
        ]
        expected_result = [
            "Adams 20",
            "Brown 30",
            "Smith 10"
        ]

        # when
        result = process_election_results(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_votes_per_candidate(self):

        # given
        data = [
            "Smith 10",
            "Brown 20",
            "Smith 15",
            "Brown 25",
            "Adams 30"
        ]
        expected_result = [
            "Adams 30",
            "Brown 45",
            "Smith 25"
        ]

        # when
        result = process_election_results(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_return_empty_list_for_no_data(self):

        # given
        data = []
        expected_result = []

        # when
        result = process_election_results(data)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_numbers(self):
        
        # given
        data = [
            "Smith 1000000000",
            "Brown 2000000000",
            "Smith 1000000000"
        ]
        expected_result = [
            "Brown 2000000000",
            "Smith 2000000000"
        ]

        # when
        result = process_election_results(data)

        # then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()


