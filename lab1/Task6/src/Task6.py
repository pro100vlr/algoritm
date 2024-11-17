import time
import psutil
from utils import read_data, write_data, input_path, output_path


def bubble_sort(arr, n):
    for i in range(n - 1): # количество итераций должно быть на 1 меньше
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Проверка корректности: массив должен быть отсортирован по возрастанию
def is_sorted(sorted_arr):
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] > sorted_arr[i + 1]:
            return False
    return True

if __name__ == '__main__':

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    n, array = read_data('Task6' + input_path)

    # Замер времени
    start_time = time.time()

    # Сортировка массива
    sorted_arr = bubble_sort(array, n)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл

    write_data('Task6' + output_path, sorted_arr)

    if is_sorted(sorted_arr):
        print("Процедура bubble_sort работает корректно, массив отсортирован.")
    else:
        print("Массив не отсортирован")
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")

