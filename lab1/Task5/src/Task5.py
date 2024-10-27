import psutil
import time

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
# Чтение данных из файла input.txt
with open('Task5/txtf/input.txt', 'r') as f:
    n = int(f.readline().strip())  # Первое число - количество элементов
    if n < 1 or n > 10**3:
      print("Неверное значение переменных")
      exit()
    array = list(map(int, f.readline().strip().split()))  # Чтение массива

# Замер времени
start_time = time.time()
# Сортировка выбором
sorted_array = selection_sort(array, n)

end_time = time.time()
mem_after = psutil.Process().memory_info().rss

# Запись результата в файл output.txt
with open('Task5/txtf/output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_array)) + '\n')
print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")

