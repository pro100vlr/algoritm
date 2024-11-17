import psutil
import time
from utils import read_data, input_path, output_path, write_data

def process_stack_commands(commands):
    stack = []
    result = []
    
    for command in commands:
        if command.startswith('+'):
            # Команда добавления числа в стек
            _, num = command.split()
            stack.append(int(num))
        elif command == '-':
            # Команда изъятия из стека и запись результата
            if stack:
                result.append(stack.pop())
                
    return result

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение команд из файла input.txt
    n, commands = read_data('Task1' + input_path)

    # Замер времени
    start_time = time.time()

    output = process_stack_commands(commands)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл output.txt
    write_data('Task1' + output_path, output)

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")