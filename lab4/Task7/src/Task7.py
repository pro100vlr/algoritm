from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab4/task7"
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

   
    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]
    m = data[2]

    assert 1 <= n <= 10**6, "Выход за пределы значений для n"
    assert 1 <= m <= n, "Выход за пределы значений для m"
    assert all(0 <= x <= 10**5 for x in arr), "Выход за пределы значений для элементов массива"

    result = ' '.join(map(str, sliding_window_maximum(arr, n, m)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(sliding_window_maximum, arr, n, m)

