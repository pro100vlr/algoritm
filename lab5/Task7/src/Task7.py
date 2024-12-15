from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab5/task7"

def max_heapify(array, n, i):
    """Итеративная процедура max-heapify для поддержания свойства кучи."""
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        # Находим наибольший элемент среди i, left и right
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right

        # Если i — не наибольший, меняем местами и продолжаем
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            i = largest
        else:
            break

def build_max_heap(array, n):
    """Строим максимальную кучу."""
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def heap_sort(array):
    """Пирамидальная сортировка."""
    n = len(array)

    # Шаг 1: построение max-heap
    build_max_heap(array, n)

    # Шаг 2: сортировка
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий максимум (корень) в конец
        array[0], array[i] = array[i], array[0]
        # Уменьшаем размер кучи и перестраиваем её
        max_heapify(array, i, 0)
    return array

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    array = data[1]
    
    assert (1 <= n <= 10**5), "Выход за пределы значений для n"
    assert all(abs(element) <= 10**9 for element in array), "Не все значения находятся в указанном диапазоне"
   
    result = heap_sort(array)
    result.reverse()
    result_str = ' '.join(map(str, result))
    
    write_data(lab_task + output_path, result_str)

    print_input_output(lab_task + input_path, result_str)

    measure(heap_sort, array)

  