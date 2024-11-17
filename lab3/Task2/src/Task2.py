import psutil
import time
from utils import write_data, output_path

def anti_quick_sort(n):    
    arr = list(range(1, n + 1))
    for i in range(2, n): 
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
    return arr
# Чтение данных из файла input.txt

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task2/txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())
        if not(n>=1 or n<=10**6):
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()
    # Замер времени
    start_time = time.time()

    
    res_arr = anti_quick_sort(n)
    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    write_data('Task2' + output_path, res_arr)
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")