import unittest
from lab5.task5.src.task5 import schedule_tasks
from utils import measure

class TestScheduleTasks(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        tasks = [1, 2, 3, 4, 5]
        n = 2
        m = 5
        expected_output = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]
        expected_time = 6
        expected_memory = 512

        # then
        result = schedule_tasks(n, m, tasks)
        time, memory = measure(schedule_tasks, n, m, tasks)

        # when
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, expected_time)
        self.assertLessEqual(memory, expected_memory)

    def test_should_assign_tasks_to_threads(self):

        # given
        n = 2
        m = 5
        tasks = [1, 2, 3, 4, 5]
        expected_result = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        # when
        result = schedule_tasks(n, m, tasks)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_single_thread(self):

        # given
        n = 1
        m = 3
        tasks = [2, 4, 6]
        expected_result = [(0, 0), (0, 2), (0, 6)]

        # when
        result = schedule_tasks(n, m, tasks)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_threads_evenly(self):

        # given
        n = 3
        m = 6
        tasks = [1, 1, 1, 1, 1, 1]
        expected_result = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]

        # when
        result = schedule_tasks(n, m, tasks)

        # then
        self.assertEqual(result, expected_result)
    
    def test_should_handle_no_tasks(self):

        # given
        n = 3
        m = 0
        tasks = []
        expected_result = []

        # when
        result = schedule_tasks(n, m, tasks)

        # then
        self.assertEqual(result, expected_result)

    def test_should_handle_large_task_times(self):
        
        # given
        n = 2
        m = 3
        tasks = [10, 20, 30]
        expected_result = [(0, 0), (1, 0), (0, 10)]

        # when
        result = schedule_tasks(n, m, tasks)

        # then
        self.assertEqual(result, expected_result)
     
if __name__ == "__main__":
    unittest.main()


        