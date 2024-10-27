import psutil
import time
import csv
from datetime import datetime

# Функция для поиска максимального пересекающего подмассива (через середину)
def find_max_crossing_subarray(prices, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    
    # Идем влево от середины
    for i in range(mid, low - 1, -1):
        sum += prices[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1
    
    # Идем вправо от середины
    for j in range(mid + 1, high + 1):
        sum += prices[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    
    return max_left, max_right, left_sum + right_sum

# Функция для поиска максимального подмассива
def find_maximum_subarray(prices, low, high):
    if low == high:
        return low, high, prices[low]  # Базовый случай: 1 элемент
    
    mid = (low + high) // 2
    
    # Рекурсивно находим максимальные подмассивы в левой и правой половинах
    left_low, left_high, left_sum = find_maximum_subarray(prices, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(prices, mid + 1, high)
    
    # Находим максимальный подмассив, который пересекает середину
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(prices, low, mid, high)
    
    # Определяем, какой из них максимальный
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

# Чтение данных из файла и фильтрация по году 2015
def load_data(file_path):
    dates = []
    prices = []
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропускаем заголовки
        for row in csv_reader:
            date_str = row[0]  # Первый столбец — дата
            price_str = row[2]  # Третий столбец — цена (максимальная за день)
            
            # Преобразуем дату и проверяем, относится ли она к 2015 году
            date = datetime.strptime(date_str, "%Y-%m-%d")
            if date.year == 2015:
                price = float(price_str)
                dates.append(date_str)
                prices.append(price)
    
    # Преобразуем цены в изменения цен, чтобы работать с ними как с массивом прибылей/убытков
    price_changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    
    return dates, price_changes

# Измеряем память
mem_before = psutil.Process().memory_info().rss

# Загрузим данные
file_path = 'Task6/txtf/aame.us.txt'
dates, price_changes = load_data(file_path)

# Замер времени
start_time = time.time()

# Найдём дни покупки и продажи с максимальной прибылью
buy_index, sell_index, max_profit = find_maximum_subarray(price_changes, 0, len(price_changes) - 1)

end_time = time.time()
mem_after = psutil.Process().memory_info().rss

# Выведем результаты
print(f"Дата покупки: {dates[buy_index]}")
print(f"Дата продажи: {dates[sell_index + 1]}")  # sell_index + 1, потому что сравнивали изменения
print(f"Максимальная прибыль за 2015 год: {max_profit :.2f}")
print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
