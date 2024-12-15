from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab1/task2"

def insertion_sort_with_position_tracking(arr, n):
    # Массив для отслеживания индексов перемещения элементов
    positions = [1] * n  # Здесь будем записывать новые индексы для каждого элемента

    # Основной алгоритм сортировки вставками
    for i in range(1, n):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1

        # Сдвигаем элементы вправо, если они больше ключевого
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Сдвигаем элементы
            j -= 1

        arr[j + 1] = key  # Вставляем ключ на нужную позицию

        # Фиксируем позицию, куда вставлен элемент на каждом шаге (с прибавкой 1)
        positions[i] = j + 2  # Увеличиваем индекс на 1, чтобы соответствовать задаче

    return positions, arr

if __name__ == "__main__":
    
    data = read_file_data(lab_task + input_path)
    n = data[0]
    arr = data[1]
    
    result = "\n".join(" ".join(map(str, array)) for array in insertion_sort_with_position_tracking(arr, n))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(insertion_sort_with_position_tracking, arr, n)
