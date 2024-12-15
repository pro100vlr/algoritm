from utils import read_file_data, write_data, input_path, output_path, print_input_output, measure

lab_task = "lab7/Task5"

def longest_common_subsequence(a, b, c, n, m, l):

    # Инициализация трёхмерного массива для хранения длины LCS
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    # Динамическое программирование
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]

if __name__ == "__main__":
    # Чтение данных из файла
    data = read_file_data(lab_task + input_path)
    n, m, l = data[0], data[2], data[4]
    A = [data[1]] if isinstance(data[1], int) else data[1]
    B = [data[3]] if isinstance(data[3], int) else data[3]
    C = [data[5]] if isinstance(data[5], int) else data[5]

    assert(1 <= n <= 100) and (1 <= m <= 100) and (1 <= l <= 100), "Выход за пределы значений для n, m и l"
    assert all(-10**9 < element < 10**9 for element in A), "Не все значения находятся в пределах от -10**9 до 10**9"
    assert all(-10**9 < element < 10**9 for element in B), "Не все значения находятся в пределах от -10**9 до 10**9"
    assert all(-10**9 < element < 10**9 for element in C), "Не все значения находятся в пределах от -10**9 до 10**9"


    # Решение задачи
    result = longest_common_subsequence(A, B, C, n, m, l)

    # Запись результата в файл
    write_data(lab_task + output_path, str(result))

    # Вывод данных для отладки
    print_input_output(lab_task + input_path, str(result))

    # Замер времени выполнения
    measure(longest_common_subsequence, A, B, C, n, m, l)