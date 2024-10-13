import time 
import psutil
t_start=time.perf_counter()
def linear_search(arr, target):
    indices = []  # Список для хранения индексов
    for i in range(len(arr)):
        if arr[i] == target:  # Если текущий элемент равен целевому
            indices.append(i)  # Добавляем индекс в список
    return indices  # Возвращаем список индексов

# Чтение данных из входного файла
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task4/input.txt', 'r') as f:
    # Чтение первой строки и преобразование в список строк
    numbers = list(map(int, f.readline().strip().split()))
    # Чтение второй строки (число V)
    target_number = int(f.readline().strip())
    if len(numbers) < 1 or len(numbers) > 10**3 or target_number < -10**3 or target_number > 10**3:
      print("Неверное значение переменных")
      exit()
     # Проверка, что все элементы массива в пределах [-1000, 1000]
    if not all(-10**3 <= x <= 10**3 for x in numbers):
        print("Элементы массива выходят за пределы допустимого диапазона")
        exit()

# Поиск индексов целевого числа
found_indices = linear_search(numbers, target_number)

# Проверяем, сколько раз встречается число
count = len(found_indices)

# Запись результата в выходной файл
with open('/Users/valeriya/Desktop/alg(labs)/lab1/Task4/output.txt', 'w') as f:
    if count == 1:
        f.write(str(found_indices[0]))
    elif count > 1:
        indices_str = ', '.join(map(str, found_indices))  # Преобразуем индексы в строку
        f.write(str(count) + "\n" + indices_str)  # Записываем количество и индексы
    else:
        f.write("-1")  # Если число не найдено
print("Время работы: %s секунд" %(time.perf_counter()- t_start))
print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f}МБ")
