import time
import tracemalloc

def read_file_data(input_path: str): # прочитать и преобразовать содержимое input.txt
    data = []
    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Проверяем, является ли строка числом
            if line.lstrip('-').isdigit():
                data.append(int(line))
            else:
                # Пробуем преобразовать строку в список чисел
                parts = line.split()
                try:
                    numbers = [int(part) for part in parts]
                    data.append(numbers if len(numbers) > 1 else numbers[0])
                except ValueError:
                    # Если преобразование не удалось, добавляем строку как есть
                    data.append(line)
                    
    return data

def write_data(output_path: str, result: str): # распечатать результат в output.txt
    with open(output_path, 'w') as file:
        file.write(result)

def print_input_output(input_path, result): # вывести содержимое входного и выходного файлов
    with open(input_path, 'r') as f:
        input_file = f.readlines()

    print("Содержимое input.txt:")
    for line in input_file:
        print(line.strip())

    print("Запись в output.txt:\n" + result)

input_path = '/txtf/input.txt'
output_path = '/txtf/output.txt'

def measure(func, *args):
    """
    Функция для измерения времени и пикового использования памяти.

    :param func: Функция, которую нужно замерить.
    :param args: Аргументы для функции.
    :return: Результат выполнения функции.
    """
    tracemalloc.start()  # Старт отслеживания памяти
    start = time.perf_counter()  # Точнее, чем time.time() для замеров
    _ = func(*args)  # Выполняем функцию
    elapsed_time = time.perf_counter() - start  # Конец замера времени

    _, peak_memory = tracemalloc.get_traced_memory()  # Пиковая память
    tracemalloc.stop()  # Останавливаем отслеживание памяти

    # Печатаем результаты
    print(f"Время работы: {elapsed_time:.6f} с")
    print(f"Использование памяти: {peak_memory / 1024**2:.6f} МБ\n")

    return elapsed_time, peak_memory / 1024**2

