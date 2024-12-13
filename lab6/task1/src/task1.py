from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab6/Task1"

def process_operations(operations):
    result = []
    elements = set()  # Наше множество
    
    for operation in operations:
        command, x = operation[0], int(operation[1])
        
        if command == "A":  # Добавление элемента
            elements.add(x)
        elif command == "D":  # Удаление элемента
            elements.discard(x)
        elif command == "?":  # Проверка существования
            result.append("Y" if x in elements else "N")
    
    return result


if __name__ == "__main__":    

    data = read_file_data(lab_task + input_path)
    n = data[0]
    assert n <= 10**5, "Слишком много операций!"
    operations = [line.split() for line in data[1:]]
    
    result = '\n'.join(process_operations(operations))
    
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(process_operations, operations)