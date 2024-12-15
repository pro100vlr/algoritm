from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab3/task4"

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

   data = read_file_data(lab_task + input_path)
    
   s, p = data[0]
   segments = data[1:-1]
   points = data[-1]

   assert 1 <= s <= 50000 and 1 <= p <= 50000, "Выход за пределы значений для s и p"
   assert all(all(abs(num) <= 10**8 for num in row) for row in data), "Не все значения находятся в указанном диапазоне"
   assert all(abs(point) <= 10**8 for point in points), "Не все значения находятся в указанном диапазоне"

   result = ' '.join(map(str, count_segments_containing_points(segments, points)))

   write_data(lab_task + output_path, result)

   print_input_output(lab_task + input_path, result)

   measure(count_segments_containing_points, segments, points)























