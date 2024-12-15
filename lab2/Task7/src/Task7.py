import time 
import psutil 
from lab2.task6.src.task6 import load_data, file_path 
 
def max_subarray_with_indices(arr): 
    max_sum = arr[0] 
    current_sum = arr[0] 
    start = end = 0  # Конечные индексы максимального подмассива 
    temp_start = 0   # Временный начальный индекс для текущего подмассива 
 
    for i in range(1, len(arr)): 
        if arr[i] > current_sum + arr[i]: 
            current_sum = arr[i] 
            temp_start = i 
        else: 
            current_sum += arr[i] 
         
        # Обновляем max_sum и индексы, если нашли новый максимальный подмассив 
        if current_sum > max_sum: 
            max_sum = current_sum 
            start = temp_start 
            end = i 
 
    return max_sum, start, end 
 
#тестируем аналогично задаче №6 
if __name__ == '__main__': 
    # Измеряем память 
    mem_before = psutil.Process().memory_info().rss 
 
    dates, price_changes = load_data(file_path) 
 
    # Замер времени 
    start_time = time.time() 
 
    max_sum, start, end = max_subarray_with_indices(price_changes) 
 
    end_time = time.time() 
    mem_after = psutil.Process().memory_info().rss 
 
    # Выведем результаты 
    print(f"Дата покупки: {dates[start]}") 
    print(f"Дата продажи: {dates[end + 1]}")  
    print(f"Максимальная прибыль за 2015 год: {max_sum :.2f}") 
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")