import time 
import psutil
t_start=time.perf_counter()
def insertion_sort_descending(arr):

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Вставляем элемент на его место, используя swap
        # Будем делать swap, пока не найдем правильную позицию для key
        while j >= 0 and arr[j] < key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]  # Обмениваем элементы (swap)
            j -= 1
    
    return arr

# Чтение данных из файла input.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task3/input.txt', 'r') as f:
    n = int(f.readline().strip())  # Первое число - количество элементов
    if n < 1 or n > 10**3:
      print("Неверное значение переменных")
      exit()
    array = list(map(int, f.readline().strip().split()))  # Чтение массива

sorted_array = insertion_sort_descending(array)

# Запись результата в файл output.txt
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task3/output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_array)))
print("Время работы: %s секунд" %(time.perf_counter()- t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f}МБ")

