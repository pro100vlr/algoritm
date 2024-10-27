import psutil
import time

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Индекс для левой части
    j = mid + 1 # Индекс для правой части
    k = left    # Индекс для временного массива
    inv_count = 0
    
    # Слияние двух половин
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # Все оставшиеся элементы в левой части arr[i...mid] больше чем arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1) # Все эти элементы образуют инверсии
            j += 1
        k += 1

    # Копируем оставшиеся элементы левой половины, если есть
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы правой половины, если есть
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)     # Считаем инверсии в левой половине
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right) # Считаем инверсии в правой половине
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)   # Сливаем и считаем инверсии в процессе

    return inv_count

if __name__ == '__main__':
    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из входного файла
    with open('Task3/txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    # Замер времени
    start_time = time.time()

    temp_arr = [0] * n  # Временный массив
    result = merge_sort_and_count(arr, temp_arr, 0, n - 1)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результатов в выходной файл
    with open('Task3/txtf/output.txt', 'w') as f:
        f.write(str(result))
    
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")

