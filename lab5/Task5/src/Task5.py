import heapq
import psutil
import time

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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение входных данных
    with open("Task5/txtf/input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        tasks = list(map(int, f.readline().split()))

    # Замер времени
    start_time1 = time.time()

    # Решение задачи
    result = schedule_tasks(n, m, tasks)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись выходных данных
    with open("Task5/txtf/output.txt", "w") as f:
        for thread_index, start_time in result:
            f.write(f"{thread_index} {start_time}\n")

    print(f"Время работы: {end_time - start_time1 :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
    

