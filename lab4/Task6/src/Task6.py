import psutil
import time
from collections import deque

from utils import read_data, write_data, input_path, output_path

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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение команд из файла input.txt    
    n, commands = read_data('Task6' + input_path)

     # Замер времени
    start_time = time.time()

    output = process_commands(commands)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл output.txt
    write_data('Task6' + output_path, output)

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")