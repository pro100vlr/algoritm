import psutil
import time
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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task8/txtf/input.txt', 'r') as f:
        n, K = map(int, f.readline().strip().split())
        if not(n>=1 and n<=10**5):
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()
       # Считываем точки
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().strip().split())
            if not(-10**8<= x <= y <= 10**8):
                print('Элементы массива выходят за пределы допустимого диапазона')
                exit()
            points.append((x, y))

    # Замер времени
    start_time = time.time()

    res_points= k_closest_points(points, K)
    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task8/txtf/output.txt', 'w') as f:
        formatted_points = ",".join(f"[{x},{y}]" for x, y in res_points)
        f.write(formatted_points)
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")