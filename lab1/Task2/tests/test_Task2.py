import unittest
from lab1.task2.src.task2 import insertion_sort_with_position_tracking
from utils import measure

class TestInsertionSortWithPositionTracking(unittest.TestCase):
    def test_should_check_time_and_memory(self):
        
        # given
        n = 10
        arr = ['1', '8', '4', '2', '3', '7', '5', '6', '9', '0']
        # Приводим ожидаемый вывод к тому же формату
        expected_output = [
            [1, 2, 2, 2, 3, 5, 5, 6, 9, 1],  # Список чисел
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # Список чисел
        ]
        expected_time = 2  # Ограничение времени выполнения
        expected_memory = 256  # Ограничение памяти в МБ

        # when
        result = insertion_sort_with_position_tracking(arr, n)  # Выполняем сортировку
        time, memory = measure(insertion_sort_with_position_tracking, arr, n)  # Замеры

        # Приводим результат в подходящий формат (если нужно)
        # Убеждаемся, что возвращаются числа, а не строки
        formatted_result = [
            list(map(int, result[0])),  # Преобразуем первую часть к списку чисел
            list(map(int, result[1]))  # Преобразуем вторую часть к списку чисел
        ]

        # then
        self.assertEqual(formatted_result, expected_output)  # Проверяем соответствие результата
        self.assertLessEqual(time, expected_time)  # Время не превышает ожидаемое
        self.assertLessEqual(memory, expected_memory)  # Память не превышает лимит

    def test_should_sort_and_track_positions_basic_case(self):
        
        # given
        arr = [4, 3, 2, 1]
        n = len(arr)
        expected_positions = [1, 1, 1, 1]  
        expected_sorted_array = [1, 2, 3, 4]

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

    def test_should_sort_and_track_positions_already_sorted(self):
        
        # given
        arr = [1, 2, 3, 4]
        n = len(arr)
        expected_positions = [1, 2, 3, 4]  
        expected_sorted_array = [1, 2, 3, 4]

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

    def test_should_sort_and_track_positions_reverse_sorted(self):
        
        # given
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        expected_positions = [1, 1, 1, 1, 1]  
        expected_sorted_array = [1, 2, 3, 4, 5]

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

    def test_should_sort_and_track_positions_with_duplicates(self):
        
        # given
        arr = [4, 2, 2, 4, 1]
        n = len(arr)
        expected_positions = [1, 1, 2, 4, 1]  
        expected_sorted_array = [1, 2, 2, 4, 4]

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

    def test_should_sort_and_track_positions_single_element(self):
        
        # given
        arr = [42]
        n = len(arr)
        expected_positions = [1]  
        expected_sorted_array = [42]

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

    def test_should_sort_and_track_positions_empty_array(self):
        
        # given
        arr = []
        n = len(arr)
        expected_positions = []  
        expected_sorted_array = []

        # when
        positions, sorted_array = insertion_sort_with_position_tracking(arr, n)

        # then
        self.assertEqual(positions, expected_positions)
        self.assertEqual(sorted_array, expected_sorted_array)

if __name__ == "__main__":
    unittest.main()
