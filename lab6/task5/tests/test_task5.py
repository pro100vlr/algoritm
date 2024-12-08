import unittest
from lab6.task5.src.task5 import process_election_results
from utils import measure

class Test(unittest.TestCase):

    expected_time = 2
    expected_memory = 64

    def test_should_process_election_results_successful_two_candidates(self):
        # given
        
        data = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expected_output = ['McCain 16', 'Obama 17']

        # then
        result = process_election_results(data)
        time, memory = measure(process_election_results, data)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_process_election_results_successful_three_candidates(self):
            # given
            
            data = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
            expected_output = ['ivanov 900', 'petr 70', 'tourist 3']
            
            # then
            result = process_election_results(data)
            time, memory = measure(process_election_results, data)

            # when
            self.assertEqual(result, expected_output)
            self.assertLessEqual(time, self.expected_time)
            self.assertLessEqual(memory, self.expected_memory)

    def test_should_process_election_results_successful_one_candidate(self):
            # given
            
            data = ['bur 1']
            expected_output = ['bur 1']
        
            # then
            result = process_election_results(data)
            time, memory = measure(process_election_results, data)

            # when
            self.assertEqual(result, expected_output)
            self.assertLessEqual(time, self.expected_time)
            self.assertLessEqual(memory, self.expected_memory)
            
if __name__ == "__main__":
    unittest.main()