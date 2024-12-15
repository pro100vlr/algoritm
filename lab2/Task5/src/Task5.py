from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab2/task5"

def find_majority_element(arr, n):
    # Первый этап: находим кандидата на большинство
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Второй этап: проверяем, является ли кандидат элементом большинства
    if arr.count(candidate) > n // 2:
        return candidate
    else:
        return None

if __name__ == '__main__':

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]

    assert (1 <= n <= 10**5), "Выход за пределы значений для n"
    assert(all((abs(element) <= 10**9 for element in arr))), "Не все значения находятся в указанном диапазоне"

    result = str(1 if find_majority_element(arr, n) is not None else 0)

    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(find_majority_element, arr, n)