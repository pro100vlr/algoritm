import psutil
import time
from utils import write_data, output_path
def count_segments_containing_points(segments, points):
    # Разделение отрезков на начала и концы
    starts = sorted([segment[0] for segment in segments])
    ends = sorted([segment[1] for segment in segments])

    # Сортировка точек и сохранение их исходного индекса
    points = sorted((point, idx) for idx, point in enumerate(points))
    result = [0] * len(points)

    # Инициализация указателей
    s_ptr, e_ptr = 0, 0
    active_segments = 0

    # Обход точек и подсчёт активных отрезков
    for point, idx in points:
        # Увеличиваем активные отрезки, если начало отрезка <= точка
        while s_ptr < len(starts) and starts[s_ptr] <= point:
            active_segments += 1
            s_ptr += 1

        # Уменьшаем активные отрезки, если конец отрезка < точка
        while e_ptr < len(ends) and ends[e_ptr] < point:
            active_segments -= 1
            e_ptr += 1

        # Сохраняем результат для текущей точки
        result[idx] = active_segments

    return result


if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task4/txtf/input.txt', 'r') as f:
        s, p = map(int, f.readline().strip().split())
        if not(1<= s <= 50000 and 1<= p <= 50000 ):
            print('Неверные значения переменных')
            exit()
       # Считываем отрезки
        segments = []
        for _ in range(s):
            l, r = map(int, f.readline().strip().split())
            if not(-10**8<= l <= r <= 10**8):
                print('Элементы массива выходят за пределы допустимого диапазона')
                exit()
            segments.append((l, r))
        # Считываем точки
        points = list(map(int, f.readline().strip().split()))
        if not(all(-10**8<= x <= 10**8 for x in points)):
            print('Элементы массива выходят за пределы допустимого диапазона')
            exit() 

    # Замер времени
    start_time = time.time()

  
    res_arr = count_segments_containing_points(segments, points)
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    write_data('Task4' + output_path, res_arr)
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")