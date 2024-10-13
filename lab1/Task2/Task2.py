import time 
import psutil
t_start=time.perf_counter()
def insertion_sort_with_position_tracking(arr):
    # Массив для отслеживания индексов перемещения элементов
    positions = [1] * n  # Здесь будем записывать новые индексы для каждого элемента

    # Основной алгоритм сортировки вставками
    for i in range(1, n):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1

        # Сдвигаем элементы вправо, если они больше ключевого
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Сдвигаем элементы
            j -= 1

        arr[j + 1] = key  # Вставляем ключ на нужную позицию

        # Фиксируем позицию, куда вставлен элемент на каждом шаге (с прибавкой 1)
        positions[i] = j + 2  # Увеличиваем индекс на 1, чтобы соответствовать задаче

    return positions, arr

# Чтение данных из файла input.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task2/input.txt', 'r') as f:
    n = int(f.readline().strip())  # Число элементов
    arr = list(map(int, f.readline().strip().split()))  # Массив чисел

# Вызов функции сортировки
positions, sorted_arr = insertion_sort_with_position_tracking(arr)

# Запись результатов в файл output.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task2/output.txt', 'w') as f:
    f.write(' '.join(map(str, positions)) + '\n')  # Массив индексов
    f.write(' '.join(map(str, sorted_arr)) + '\n')  # Отсортированный массив
print("Время работы: %s секунд" %(time.perf_counter()- t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f}МБ")
