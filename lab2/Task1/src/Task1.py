import psutil
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Сортируем левую и правую части
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Процедура слияния без использования сигнальных значений
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы из L (если есть)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы из R (если есть)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Чтение данных из файла input.txt

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task1/txtf/input.txt', 'r') as file:
        n = int(file.readline().strip())
        if not(n >= 1 or n <= 2*10**4):
            print("Неверное значение переменных")
            exit()
        arr = list(map(int, file.readline().strip().split()))
        if not all(abs(x) <= 10**9 for x in arr):
            print("Элементы массива выходят за пределы допустимого диапазона")
            exit()

    # Замер времени
    start_time = time.time()

    # Сортировка слиянием
    sorted_arr = merge_sort(arr)

    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task1/txtf/output.txt', 'w') as file:
        file.write(' '.join(map(str, sorted_arr)) + '\n')
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")