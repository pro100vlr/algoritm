import psutil
import time
from utils import read_data, input_path
def is_heap(n, array):
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Проверяем левый потомок
        if left < n and array[i] > array[left]:
            return "NO"
        
        # Проверяем правый потомок
        if right < n and array[i] > array[right]:
            return "NO"
    
    return "YES"

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из файла
    n, array = read_data('Task1' + input_path, 10**6, 2*10**9)
    # Замер времени
    start_time = time.time()

    # Определение результата
    result = is_heap(n, array)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл
    with open("Task1/txtf/output.txt", "w") as f:
        f.write(result + "\n")
        
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
    