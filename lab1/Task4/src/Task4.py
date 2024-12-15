from utils import read_file_data, write_data, input_path, output_path, print_input_output, measure

lab_taks = 'lab1/task4'

def linear_search(arr, target):
    indices = []  # Список для хранения индексов
    for i in range(len(arr)):
        if arr[i] == target:  # Если текущий элемент равен целевому
            indices.append(i+1)  # Добавляем индекс в список

    count = len(indices)

    if count == 1:
        result = str(indices[0])
    elif count > 1:
        indices_str = ', '.join(map(str, indices))  # Преобразуем индексы в строку
        result = str(count) + "\n" + indices_str  # Записываем количество и индексы
    else:
        result = "-1"  # Если число не найдено

    return result

if __name__ == "__main__":
   
    data_numbers = read_file_data(lab_taks + input_path)
    data_pig = read_file_data(lab_taks + '/txtf/input_pig.txt')

    # считывание для числового массива
    numbers = data_numbers[0]
    target_number = data_numbers[1]

    assert (1 <= len(numbers) <= 10**3), "Выход за пределы значений для n"
    assert (all(abs(element) <= 10**3 for element in numbers)), "Не все значения находятся в указанном диапазоне"

    # считывание для строкового списка
    animals = data_pig[0].split()
    target_pig = data_pig[1]

    result_numbers = linear_search(numbers, target_number)
    result_pig = linear_search(animals, target_pig)

    write_data(lab_taks + output_path, result_numbers)
    write_data(lab_taks + '/txtf/output_pig.txt', result_pig)

    print_input_output(lab_taks + input_path, result_numbers)
    print_input_output(lab_taks + '/txtf/input_pig.txt', result_pig)

    measure(linear_search, numbers, target_number)

