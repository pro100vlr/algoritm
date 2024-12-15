from utils import read_file_data, write_data, input_path, output_path, print_input_output, measure

lab_task = "lab7/Task1"

def min_coins(money, coins):
    # Инициализация массива для хранения минимального количества монет для каждой суммы
    dp = [float('inf')] * (money + 1)
    dp[0] = 0  # Для суммы 0 нужно 0 монет

    # Основной цикл динамического программирования
    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # Если dp[money] осталось равным бесконечности, значит размен невозможен
    return dp[money] if dp[money] != float('inf') else -1

if __name__ == "__main__":
    # Чтение данных из файла
    data = read_file_data(lab_task + input_path)
    money, k = data[0]
    coins = data[1]

    assert(1 <= money <= 10**3) and (1 <= k <= 100), "Выход за пределы значений для money и k"
    assert all(1 <= coin <= 10**3 for coin in coins), "Не все значения находятся в пределах от 1 до 1000"

    # Решение задачи
    result = min_coins(money, coins)

    # Запись результата в файл
    write_data(lab_task + output_path, str(result))

    # Вывод данных для отладки
    print_input_output(lab_task + input_path, str(result))

    # Замер времени выполнения
    measure(min_coins, money, coins)
