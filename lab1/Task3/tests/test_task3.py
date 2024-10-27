from Task3.src.Task3 import insertion_sort_descending
import psutil
import time

def load_data(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        array = list(map(int, f.readline().strip().split()))
        return n, array

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        f.write(' '.join(map(str, data)))

time_list = []
mem_list = []
for input in ['input_average.txt', 'input_worst.txt', 'input_best.txt']:
    # Измеряем память перед сортировкой
    mem_before = psutil.Process().memory_info().rss

    n, input_array = load_data(f'Task3/tests/{input}')
    expected = sorted(input_array, reverse=True)

    # Замер времени перед сортировкой
    start_time = time.time()

    # Вызов функции сортировки
    result = insertion_sort_descending(input_array, n)

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