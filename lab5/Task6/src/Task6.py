import heapq
import psutil
import time

def process_operations(operations):
    heap = []  # Основная куча
    index_map = {}  # Маппинг позиции для операции D
    output = []
    current_index = 0  # Счётчик для операций `A`

    for operation in operations:
        if operation[0] == "A":
            # Добавляем элемент в кучу
            x = int(operation[1])
            heapq.heappush(heap, (x, current_index))
            index_map[current_index] = x  # Запоминаем, где находится элемент
            current_index += 1

        elif operation[0] == "X":
            # Извлекаем минимальный элемент
            if heap:
                # Удаляем элемент и обновляем маппинг
                value, idx = heapq.heappop(heap)
                output.append(str(value))
                del index_map[idx]  # Удаляем из маппинга
            else:
                output.append("*")

        elif operation[0] == "D":
            # Уменьшаем значение элемента
            x = int(operation[1]) - 1  # Индексация в Python начинается с 0
            y = int(operation[2])

            if x in index_map:
                old_value = index_map[x]
                index_map[x] = y  # Обновляем маппинг

                # Находим и удаляем старое значение в куче
                heap.remove((old_value, x))
                heapq.heapify(heap)  # Перестраиваем кучу после удаления

                # Добавляем новое значение в кучу
                heapq.heappush(heap, (y, x))

    return output

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных
    with open("Task6/txtf/input.txt", "r") as f:
        n = int(f.readline())
        operations = [f.readline().strip().split() for _ in range(n)]

    # Замер времени
    start_time = time.time()

    # Выполнение операций
    output = process_operations(operations)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результатов
    with open("Task6/txtf/output.txt", "w") as f:
        f.write("\n".join(output) + "\n")
    
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")