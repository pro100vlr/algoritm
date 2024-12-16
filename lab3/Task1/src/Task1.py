from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure
import random

lab_task = "lab3/task1"

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
    return arr

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
    return arr

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

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]
    
    assert 1 <= n <= 10**4, "Выход за пределы значений для n"
    assert all(abs(element) <= 10**9 for element in arr), "Не все значения находятся в указанном диапазоне"

    result = ' '.join(map(str, randomized_quick_sort_c_partition(arr, 0, n-1)))
    #result = ' '.join(map(str, partition(arr, low, high)))
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(partition, arr, 0, n-1)
    


