from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab4/task1"

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

    data = read_file_data(lab_task + input_path)
    
    M = data[0]
    commands = data[1:]

    assert 1 <= M <= 10**6, "Выход за пределы значений для M"

    result = '\n'.join(map(str, process_stack_commands(commands)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(process_stack_commands, commands)