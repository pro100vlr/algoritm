import time 
import psutil
t_start=time.perf_counter()
# Ввод данных
def selection_sort(arr):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Обмен местами текущего элемента и минимального
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Чтение данных из файла input.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task5/input.txt', 'r') as f:
    n = int(f.readline().strip())  # Первое число - количество элементов
    if n < 1 or n > 10**3:
      print("Неверное значение переменных")
      exit()
    array = list(map(int, f.readline().strip().split()))  # Чтение массива

# Сортировка выбором
sorted_array = selection_sort(array)

# Запись результата в файл output.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task5/output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_array)) + '\n')
print("Время работы: %s секунд" %(time.perf_counter()- t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f}МБ")

