import psutil
import time
from collections import deque

def sliding_window_maximum(arr, n, m):
    result = []
    dq = deque()  # deque для хранения индексов элементов
    
    for i in range(n):
        # Удаляем элементы из deque, которые выходят за пределы текущего окна
        if dq and dq[0] < i - m + 1:
            dq.popleft()
        
        # Удаляем из deque все элементы, которые меньше текущего элемента arr[i]
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        # Добавляем текущий индекс в deque
        dq.append(i)
        
        # Добавляем в результат значение по индексу в начале deque, если окно заполнено
        if i >= m - 1:
            result.append(arr[dq[0]])
    
    return result

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из файла input.txt
    with open('Task7/txtf/input.txt', 'r') as file:
        n = int(file.readline().strip())
        if not(1 <= n <= 10**5):
            print("Количество элементов в массиве выходит за пределы допустимого диапазона")
            exit()
        arr = list(map(int, file.readline().strip().split()))
        if not(1 <= len(arr) <= 10**5):
            print("Количество элементов в массиве выходит за пределы допустимого диапазона")
            exit()
        m = int(file.readline().strip())
        if not(1 <= m <= n):
            print("Количество элементов в окне выходит за пределы допустимого диапазона")
            exit()
    
     # Замер времени
    start_time = time.time()

    result = sliding_window_maximum(arr, n, m)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл output.txt
    with open('Task7/txtf/output.txt', 'w') as file:
        file.write(" ".join(map(str, result)) + "\n")
        
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")