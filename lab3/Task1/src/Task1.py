import random
import psutil
import time
from utils import  write_data, read_data, input_path, output_path

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Ставим случайный элемент на последнее место
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

def c_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]  # Выбираем случайный элемент как опорный
    pivot = arr[low]
    
    lt = low  # Элементы меньше опорного
    gt = high  # Элементы больше опорного
    i = low + 1

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    return lt, gt

def randomized_quick_sort_c_partition(arr, low, high):
    if low < high:
        lt, gt = c_partition(arr, low, high)
        randomized_quick_sort_c_partition(arr, low, lt - 1)
        randomized_quick_sort_c_partition(arr, gt + 1, high)
    return arr

# Чтение данных из файла input.txt

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    n, array = read_data('Task1' + input_path, 10**4, 10**9)
    

    # Замер времени
    start_time = time.time()

    # Сортировка слиянием
    sorted_arr = randomized_quick_sort_c_partition(array, 0, n - 1)

    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    write_data('Task1' + output_path, sorted_arr)
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
    