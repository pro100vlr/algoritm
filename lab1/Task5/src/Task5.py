import psutil
import time
from utils import read_data, write_data, input_path, output_path

def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Обмен местами текущего элемента и минимального
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Измеряем память
mem_before = psutil.Process().memory_info().rss

n, array = read_data('Task5' + input_path)
if n < 1 or n > 10**3:
    print("Неверное значение переменных")
    exit()

# Замер времени
start_time = time.time()
# Сортировка выбором
sorted_array = selection_sort(array, n)

end_time = time.time()
mem_after = psutil.Process().memory_info().rss

write_data('Task5' + output_path, sorted_array)

print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")

