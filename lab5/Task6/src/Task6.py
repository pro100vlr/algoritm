import heapq
from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab5/task6"

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

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    operations = [operation.split() for operation in data[1:]]
    
    assert 1 <= n <= 10**6, "Слишком много операций!"
    
    result = ' '.join(map(str, process_operations(operations)))
    
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(process_operations, operations)

