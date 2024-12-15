from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab2/task4"

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Проверяем, равно ли среднее значение искомому
        if arr[mid] == target:
            return mid  # Индекс найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Если элемент не найден

if __name__ == '__main__':
    
    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    sorted_array = data[1]
    k  = data[2]
    targets = data[3]

    assert (1 <= n <= 10**5) and (1 <= k <= 10**5), "Выход за пределы значений для n и k"
    assert(all(1 <= element <= 10**9 for element in sorted_array)), "Не все значения находятся в указанном диапазоне"

    results = []
    for target in targets:
        index = binary_search(sorted_array, target)
        results.append(index)

    results_str = ' '.join(map(str, results))
   
    write_data(lab_task + output_path, results_str)

    print_input_output(lab_task + input_path, results_str)

    measure(binary_search, sorted_array, targets[0])
  
  

    