from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure
from collections import defaultdict

lab_task = "lab6/task7"

def count_beautiful_pairs(n, k, s, pairs):
    """
    Подсчитывает количество "красивых" пар в строке S.
    
    :param n: Длина строки S.
    :param k: Количество пар, которые шах считает красивыми.
    :param s: Строка из n символов.
    :param pairs: Список красивых пар.
    :return: Количество красивых пар (целое число).
    """
    # Преобразуем пары в множество для быстрого поиска
    beautiful_pairs = set(pairs)
    
    # Словарь для хранения частоты каждого символа
    freq = defaultdict(int)
    count = 0
    
    # Проход по строке S
    for char in s:
        # Для текущего символа `char` проверяем возможные пары
        for other_char in freq:
            if (other_char, char) in beautiful_pairs:
                count += freq[other_char]
        
        # Увеличиваем частоту текущего символа
        freq[char] += 1
    
    return count

if __name__ == "__main__":
    # Считываем данные из файла
    data = read_file_data(lab_task + input_path)
    
    # Корректируем парсинг данных
    n, k = data[0]  # Поскольку data[0] уже список [n, k]
    assert (1 <= n <= 100000) and (1 <= k <= 676), "Выход за пределы значений для n и k"
    s = data[1]     # Строка S — второй элемент
    pairs = [tuple(line) for line in data[2:]]  # Красивые пары
    
    # Обрабатываем данные
    result = count_beautiful_pairs(n, k, s, pairs)
    
    # Записываем результат в файл
    write_data(lab_task + output_path, str(result))
    
    # Печатаем входные и выходные данные
    print_input_output(lab_task + input_path, str(result))
    
    # Замеряем производительность функции
    measure(count_beautiful_pairs, n, k, s, pairs)
