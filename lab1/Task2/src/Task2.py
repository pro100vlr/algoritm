import psutil
import time

def insertion_sort_with_position_tracking(arr, n):
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



# Измеряем память
mem_before = psutil.Process().memory_info().rss
# Чтение данных из файла input.txt
with open('Task2/txtf/input.txt', 'r') as f:
    n = int(f.readline().strip())  # Число элементов
    arr = list(map(int, f.readline().strip().split()))  # Массив чисел

start_time = time.time()
# Вызов функции сортировки
positions, sorted_arr = insertion_sort_with_position_tracking(arr, n)

end_time = time.time()
mem_after = psutil.Process().memory_info().rss

# Запись результатов в файл output.txt
with open('Task2/txtf/output.txt', 'w') as f:
    f.write(' '.join(map(str, positions)) + '\n')  # Массив индексов
    f.write(' '.join(map(str, sorted_arr)) + '\n')  # Отсортированный массив

print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
