from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

# Указание пути к задаче
lab_task = "lab6/task4"

def put_element(data, order, key, value):
    """Добавить элемент в ассоциативный массив."""
    if key in data:
        data[key] = value
    else:
        data[key] = value
        order.append(key)

def get_element(data, key):
    """Получить элемент из ассоциативного массива."""
    return data.get(key, "<none>")

def prev_element(data, order, key):
    """Получить предыдущий элемент относительно заданного ключа."""
    if key not in data:
        return "<none>"
    index = order.index(key)
    return data[order[index - 1]] if index > 0 else "<none>"

def next_element(data, order, key):
    """Получить следующий элемент относительно заданного ключа."""
    if key not in data:
        return "<none>"
    index = order.index(key)
    return data[order[index + 1]] if index < len(order) - 1 else "<none>"

def delete_element(data, order, key):
    """Удалить элемент из ассоциативного массива."""
    if key in data:
        del data[key]
        order.remove(key)

def process_operations(operations):
    """
    Обработка операций над ассоциативным массивом.
    
    :param operations: Список операций.
    :return: Результаты операций get, prev, next.
    """
    data = {}  # Ассоциативный массив
    order = []  # Порядок добавления ключей
    result = []

    for operation in operations:
        command = operation[0]
        key = operation[1] if len(operation) > 1 else None
        value = operation[2] if len(operation) > 2 else None

        if command == "put":
            put_element(data, order, key, value)
        elif command == "get":
            result.append(get_element(data, key))
        elif command == "prev":
            result.append(prev_element(data, order, key))
        elif command == "next":
            result.append(next_element(data, order, key))
        elif command == "delete":
            delete_element(data, order, key)
    
    return result

if __name__ == "__main__":
    # Считываем данные из файла
    data = read_file_data(lab_task + input_path)
    n = data[0]
    assert n <= 10**5, "Слишком много операций!"

    # Преобразуем строки в список операций
    operations = [line.split() for line in data[1:]]
    for operation in operations:
        if not(len(operation[0]) >= 1 and len(operation[1]) >= 1 and len(operation[0]) <=20 and len(operation[1]) <= 20):
            print("Количество символов в паре(ключ, значение) должно быть от 1 до 20!")
            exit()
    # Обрабатываем операции и получаем результат
    result = '\n'.join(process_operations(operations))

    # Записываем результат в файл
    write_data(lab_task + output_path, result)
    # Печатаем входные и выходные данные
    print_input_output(lab_task + input_path, result)
    # Замеряем производительность функции
    measure(process_operations, operations)