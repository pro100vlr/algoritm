import psutil
import time

def linear_search(arr, target):
    indices = []  # Список для хранения индексов
    for i in range(len(arr)):
        if arr[i] == target:  # Если текущий элемент равен целевому
            indices.append(i+1)  # Добавляем индекс в список
    return indices  # Возвращаем список индексов


if __name__ == "__main__":
    # Чтение данных из входного файла
    with open('Task4/txtf/input.txt', 'r') as f:

        # Измеряем память
        mem_before = psutil.Process().memory_info().rss

        # Чтение первой строки и преобразование в список строк
        numbers = list(map(int, f.readline().strip().split()))
        # Чтение второй строки (число V)
        target_number = int(f.readline().strip())
        if len(numbers) < 0 or len(numbers) > 10**3 or target_number < -10**3 or target_number > 10**3:
            print("Неверное значение переменных")
        exit()
        # Проверка, что все элементы массива в пределах [-1000, 1000]
        if not all(-10**3 <= x <= 10**3 for x in numbers):
            print("Элементы массива выходят за пределы допустимого диапазона")
            exit()

    # Для строковых списков (поиск свиньи)
    with open('Task4/txtf/input_pig.txt', 'r', encoding='utf-8') as f:
        words = list(map(str, f.readline().strip().split()))
        target = f.readline().strip()

        if len(numbers) < 0 or len(numbers) > 10**3:
            print("Неверное значение переменных")
        exit()


    # Замер времени
    start_time = time.time()
    # Поиск индексов целевого числа
    found_indices = linear_search(numbers, target_number)
    found_pig = linear_search(words, target)

    # Проверяем, сколько раз встречается число
    count = len(found_indices)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в выходной файл
    with open('Task4/txtf/output.txt', 'w') as f:
        if count == 1:
            f.write(str(found_indices[0]))
        elif count > 1:
            indices_str = ', '.join(map(str, found_indices))  # Преобразуем индексы в строку
            f.write(str(count) + "\n" + indices_str)  # Записываем количество и индексы
        else:
            f.write("-1")  # Если число не найдено

    with open('Task4/txtf/output_pig.txt', 'w') as f:
        f.write(str(found_pig[0]))

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
