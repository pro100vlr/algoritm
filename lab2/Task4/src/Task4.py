import psutil
import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Проверяем, равно ли среднее значение искомому
        if arr[mid] == target:
            return mid  # Индекс найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Если элемент не найден

if __name__ == '__main__':
    
    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из входного файла
    with open('Task4/txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())
        if not(n >= 1 or n <= 10**5):
            print("Неверное значение переменных")
            exit()
        sorted_array = list(map(int, f.readline().split()))
        if not all(1 <= x <= 10**9 for x in sorted_array):     ### ТУТ ЕЩЕ НАДО ПРОВЕРИТЬ, ЧТО ЧИСЛА В МАССИВЕ РАЗЛИЧНЫ
            print("Элементы массива выходят за пределы допустимого диапазона")
            exit()
        k = int(f.readline().strip())
        if not(k >= 1 or k <= 10**5):
            print("Неверное значение переменных")
            exit()
        targets = list(map(int, f.readline().split()))
        if not all(1 <= x <= 10**9 for x in targets):
            print("Элементы массива выходят за пределы допустимого диапазона")
            exit()

    
    # Замер времени
    start_time = time.time()
    # Ищем каждый элемент из targets в отсортированном массиве sorted_array
    results = []
    for target in targets:
        index = binary_search(sorted_array, target)
        results.append(index)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результатов в выходной файл
    with open('Task4/txtf/output.txt', 'w') as f:
        f.write(' '.join(map(str, results)))

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
    