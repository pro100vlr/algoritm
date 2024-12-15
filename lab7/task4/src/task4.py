from utils import read_file_data, write_data, input_path, output_path, measure, print_input_output

lab_task = "lab7/Task4"

def longest_common_subsequence(A, B, n, m):
    # Инициализация двумерного массива для динамического программирования
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Заполнение таблицы dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

if __name__ == "__main__":
    # Чтение данных из файла
    data = read_file_data(lab_task + input_path)
    n, m = data[0], data[2]
    A = [data[1]] if isinstance(data[1], int) else data[1]
    B = [data[3]] if isinstance(data[3], int) else data[3]

    assert(1 <= n <= 100) and (1 <= m <= 100), "Выход за пределы значений для n и m"
    assert all(-10**9 < element < 10**9 for element in A), "Не все значения находятся в пределах от -10**9 до 10**9"
    assert all(-10**9 < element < 10**9 for element in B), "Не все значения находятся в пределах от -10**9 до 10**9"

    # Решение задачи
    result = longest_common_subsequence(A, B, n, m)

    # Запись результата в файл
    write_data(lab_task + output_path, str(result))

    # Вывод данных для отладки
    print_input_output(lab_task + input_path, str(result))

    # Замер времени выполнения
    measure(longest_common_subsequence, A, B, n, m)
    