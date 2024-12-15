from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab3/task8"
def k_closest_points(points, K):
    # Сортируем точки по возрастанию расстояния до начала координат
    sorted_points = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
    # Возвращаем первые K точек
    return sorted_points[:K]

# Пример данных
#points = [(1, 3), (3, 4), (2, -1), (0, 2)]
#K = 2

# Чтение данных из файла input.txt
if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)

    n, K = data[0]
    points = data[1:]

    assert 1 <= n <= 10**5 , "Выход за пределы значений для n "
    assert all(all(abs(num) <= 10**9 for num in point) for point in points), "Не все значения находятся в указанном диапазоне"

    res_points= k_closest_points(points, K)
    result = ",".join(f"[{x},{y}]" for x, y in res_points)

    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(k_closest_points, points, K)
