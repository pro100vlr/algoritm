import unittest
from lab6.Task1.src.Task1 import process_operations
from utils import measure

class Test(unittest.TestCase):
    def test_should_be_Y_N_N(self):
        # given
        
        operations = [['A', '2'], ['A', '5'], ['A', '3'], ['?', '2'], ['?', '4'], ['A', '2'], ['D', '2'], ['?', '2']]
        expected_output = ['Y', 'N', 'N']

        # then
        result = process_operations(operations)

        # when
        self.assertEqual(result, expected_output)

        # память и время для теста
        print('test_should_be_Y_N_N')
        measure(process_operations, operations)



if __name__ == "__main__":
    unittest.main()