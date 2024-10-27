import psutil
import time

def insertion_sort_descending(arr, n):

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Вставляем элемент на его место, используя swap
        # Будем делать swap, пока не найдем правильную позицию для key
        while j >= 0 and arr[j] < key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]  # Обмениваем элементы (swap)
            j -= 1
    
    return arr

if __name__ == "__main__":
    
    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из файла input.txt
    with open('Task3/txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())  # Первое число - количество элементов
        if n < 1 or n > 10**3:
            print("Неверное значение переменных")
            exit()
        array = list(map(int, f.readline().strip().split()))  # Чтение массива

    
    # Замер времени
    start_time = time.time()

    sorted_array = insertion_sort_descending(array, n)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл output.txt
    with open('Task3/txtf/output.txt', 'w') as f:
        f.write(' '.join(map(str, sorted_array)))

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")