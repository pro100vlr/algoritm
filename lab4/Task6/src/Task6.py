from collections import deque

from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab4/task6"

def process_commands(commands):
    queue = deque()         # Очередь для всех элементов
    min_queue = deque()     # Очередь для отслеживания минимальных элементов
    results = []            # Список для хранения результатов команд "?"

    for command in commands:
        if command.startswith('+'):
            # Добавление элемента в очередь
            _, num = command.split()
            num = int(num)
            queue.append(num)
            
            # Обновление min_queue
            while min_queue and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)
        
        elif command == '-':
            # Удаление элемента из очереди
            if queue:
                removed = queue.popleft()
                if min_queue and min_queue[0] == removed:
                    min_queue.popleft()
        
        elif command == '?':
            # Запрос минимума в очереди
            if min_queue:
                results.append(str(min_queue[0]))

    return results

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    M = data[0]
    commands = data[1:]

    assert 1 <= M <= 10**6, "Выход за пределы значений для M"
    
    result = '\n'.join(map(str, process_commands(commands)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(process_commands, commands)

   