import unittest
from Task5.src.Task5 import schedule_tasks
class Test(unittest.TestCase):
    def test_sliding_window_maximum(self):
        # given
        tasks = [1, 2, 3, 4, 5]
        n = 2
        m = 5
        expected_output = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        # then
        result = schedule_tasks(n, m, tasks)

        # when
        self.assertEqual(result, expected_output)
        print('Success')


if __name__ == "__main__":
    unittest.main()