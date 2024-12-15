import heapq
from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab5/task5"

def schedule_tasks(n, m, tasks):
    # Очередь с приоритетами для потоков
    heap = [(0, i) for i in range(n)]  # (время освобождения, индекс потока)
    heapq.heapify(heap)
    
    result = []
    for task_time in tasks:
        # Извлекаем поток с минимальным временем освобождения
        free_time, thread_index = heapq.heappop(heap)
        # Записываем результат для текущего задания
        result.append((thread_index, free_time))
        # Обновляем время освобождения и возвращаем поток в очередь
        heapq.heappush(heap, (free_time + task_time, thread_index))
    
    return result

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n, m = data[0]
    tasks = data[1]
    
    assert (1 <= n <= 10**6) and (1 <= m <= 10**6), "Выход за пределы значений для n и m"
    assert all(0 <= task <= 10**9 for task in tasks), "Выход за пределы значений для заданий"
    
    result = schedule_tasks(n, m, tasks)
    result_str = "\n".join(" ".join(map(str, element)) for element in result)
    
    write_data(lab_task + output_path, result_str)

    print_input_output(lab_task + input_path, result_str)

    measure(schedule_tasks, n, m, tasks)
