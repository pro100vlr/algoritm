from utils import read_file_data, write_data, input_path, output_path, print_input_output, measure

lab_task = "lab7/Task6"

def longest_increasing_subsequence(arr, n):
    # Инициализация массива для хранения длины LIS для каждого элемента
    dp = [1] * n  # dp[i] будет хранить длину LIS, заканчивающейся на i
    prev = [-1] * n  # prev[i] хранит индекс предыдущего элемента в LIS
    
    # Строим dp массив, где dp[i] - длина LIS, заканчивающейся на i
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Находим индекс максимальной длины LIS
    max_len = max(dp)
    max_index = dp.index(max_len)
    
    # Восстанавливаем саму подпоследовательность
    lis = []
    while max_index != -1:
        lis.append(arr[max_index])
        max_index = prev[max_index]
    
    lis.reverse()  # Подпоследовательность должна быть в порядке возрастания
    return max_len, lis

if __name__ == "__main__":
    # Чтение данных из файла
    data = read_file_data(lab_task + input_path)
    n = data[0]
    arr = data[1]

    assert(1 <= n <= 300000), "Выход за пределы значений для n"
    assert all(abs(element) <= 10**9 for element in arr), "Не все значения находятся в пределах от -10**9 до 10**9"

    # Решение задачи
    result_len, result_sequence = longest_increasing_subsequence(arr, n)
    

    # Запись результата в файл
    write_data(lab_task + output_path, f"{result_len}\n{' '.join(map(str, result_sequence))}")

    # Вывод данных
    print_input_output(lab_task + input_path, f"{result_len}\n{' '.join(map(str, result_sequence))}")


    # Замер времени выполнения
    measure(longest_increasing_subsequence, arr, n)