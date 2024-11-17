import psutil
import time
def can_sort_with_k_swaps(n, k, sizes):
    # Создаём отсортированную копию массива размеров
    sorted_sizes = sorted(sizes)
    
    # Проверяем, можно ли отсортировать с помощью разрешённых перестановок
    for start in range(k):
        # Получаем группу, состоящую из элементов, которые можно перемещать друг к другу
        group = sizes[start::k]
        
        # Сравниваем с отсортированной группой
        if sorted(group) != sorted_sizes[start::k]:
            return "НЕТ"
    
    return "ДА"

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task3/txtf/input.txt', 'r') as f:
        h = list(map(int, f.readline().strip().split()))
        n = h[0]
        k = h[1]
        if not(1<=n and k<=10**5):
            print('Неверные значения переменных')
            exit()
        arr = list(map(int, f.readline().strip().split()))
        if not(all(abs(x) <= 10**9 for x in arr)):
            print('Элементы массива выходят за пределы допустимого диапазона')
            exit()

    # Замер времени
    start_time = time.time()

    
    res_str = can_sort_with_k_swaps(n, k, arr)
    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task3/txtf/output.txt', 'w') as f:
        f.write(res_str )
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")