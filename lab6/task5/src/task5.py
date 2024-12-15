from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure
from collections import defaultdict

lab_task = "lab6/task5"

def process_election_results(data):
    """
    Подсчитывает количество голосов для каждого кандидата.
    
    :param data: Список строк вида "кандидат количество_голосов".
    :return: Список строк, отсортированных по фамилиям кандидатов в лексикографическом порядке.
    """
    votes = defaultdict(int)  # Используем defaultdict для подсчёта голосов
    
    for line in data:
        candidate, vote_count = line.rsplit(maxsplit=1)
        votes[candidate] += int(vote_count)
    
    # Формируем результат в лексикографическом порядке
    sorted_results = sorted(votes.items())
    return [f"{candidate} {vote_count}" for candidate, vote_count in sorted_results]

if __name__ == "__main__":
    # Считываем данные из файла
    data = read_file_data(lab_task + input_path)
    
    # Обрабатываем данные
    result = '\n'.join(process_election_results(data))
    
    # Записываем результат в файл
    write_data(lab_task + output_path, result)
    
    # Печатаем входные и выходные данные
    print_input_output(lab_task + input_path, result)
    
    # Замеряем производительность функции
    measure(process_election_results, data)
