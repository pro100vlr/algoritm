import psutil
import time
from utils import input_path, read_data
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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из файла
    n, array = read_data('Task7' + input_path, 10**5, 10**9)
    

    # Замер времени
    start_time = time.time()

    # Сортировка массива
    res_array = heap_sort(array)
    res_array.reverse()  # Для убывающего порядка

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open("Task7/txtf/output.txt", "w") as f:
        f.write(" ".join(map(str, res_array)) + "\n")

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")