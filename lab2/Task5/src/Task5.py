import psutil
import time

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

    mem_before = psutil.Process().memory_info().rss

    with open('Task5/txtf/input.txt', 'r') as file:
        n = int(file.readline().strip())     ## ДОПИСАТЬ ОГРАНИЧЕНИЯ ИЗ УСЛОВИЯ ЗАДАЧИ
        arr = list(map(int, file.readline().strip().split()))
        if not(n >= 1 and n <= 10**5):
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()
        if not(all(0 <= x <= 10**9 for x in arr)):
            print('Элементы массива выходят за пределы допустимого диапазона')
            exit()
    # Замер времени
    start_time = time.time()
    # Поиск представителя большинства
    majority_element = find_majority_element(arr, n)


    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task5/txtf/output.txt', 'w') as file:
        file.write('1' if majority_element is not None else '0')
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")