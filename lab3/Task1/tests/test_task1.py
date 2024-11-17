from Task1.src.Task1 import quick_sort, randomized_quick_sort, randomized_quick_sort_c_partition

import psutil
import time

from utils import read_data
#import sys
#sys.setrecursionlimit(3000)

def test_quick_sort(function):

    time_list = []
    mem_list = []
    for input in ['input_average.txt', 'input_worst.txt', 'input_best.txt']:
        # Измеряем память перед сортировкой
        mem_before = psutil.Process().memory_info().rss

        n, input_array = read_data(f'Task1/tests/{input}', 10**4, 10**9)
        
        expected = sorted(input_array)

        # Замер времени перед сортировкой
        start_time = time.time()

        # Вызов функции сортировки
        function(input_array, 0, n - 1)

        # Замер времени после сортировки
        end_time = time.time()
        # Измеряем память после сортировки
        mem_after = psutil.Process().memory_info().rss
        
        # Проверка соответствия результата функции и ожидаемого результата 
        assert input_array == expected, f"Test failed for {input} with {function.__name__}"

        time_list.append(end_time - start_time)
        mem_list.append(mem_after - mem_before)

    print(f"All tests passed for {function.__name__}")

    print(f"Average input case for function {function.__name__} - time: {time_list[0] :.3f} sec, memory - {mem_list[0] / 1024**2 :.3f} Мб")
    print(f"Worst input case for function {function.__name__} - time: {time_list[1] :.3f} sec, memory - {mem_list[1] / 1024**2 :.3f} Мб")
    print(f"Best input case for function {function.__name__} - time: {time_list[2] :.3f} sec, memory - {mem_list[2] / 1024**2 :.3f} Мб\n")

test_quick_sort(quick_sort)

test_quick_sort(randomized_quick_sort)

test_quick_sort(randomized_quick_sort_c_partition)