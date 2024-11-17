from Task1.src.Task1 import merge_sort
import psutil
import time

from utils import read_data

time_list = []
mem_list = []
for input in ['input_average.txt', 'input_worst.txt', 'input_best.txt']:
    # Измеряем память перед сортировкой
    mem_before = psutil.Process().memory_info().rss

    n, input_array = read_data(f'Task1/tests/{input}', 10**5, 10**9)
    
    expected = sorted(input_array)

    # Замер времени перед сортировкой
    start_time = time.time()

    # Вызов функции сортировки
    result = merge_sort(input_array)

    # Замер времени после сортировки
    end_time = time.time()
    # Измеряем память после сортировки
    mem_after = psutil.Process().memory_info().rss

    # Проверка соответствия результата функции и ожидаемого результата 
    assert result == expected

    time_list.append(end_time - start_time)
    mem_list.append(mem_after - mem_before)


print("All tests passed")
print(f"Average input case - time: {time_list[0] :.3f} sec, memory - {mem_list[0] / 1024**2 :.3f} Мб")
print(f"Worst input case - time: {time_list[1] :.3f} sec, memory - {mem_list[1] / 1024**2 :.3f} Мб")
print(f"Best input case - time: {time_list[2] :.3f} sec, memory - {mem_list[2] / 1024**2 :.3f} Мб")