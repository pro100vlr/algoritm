import psutil
import time
def h_index(citations):
    citations.sort(reverse=True)  # Сортируем по убыванию
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:  # Проверяем условие h-индекса
            h = i + 1
        else:
            break
    return h

# Чтение данных из файла input.txt

if __name__ == "__main__":

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task5/txtf/input.txt', 'r') as f:
        citations=list(map(int, f.readline().strip().split(',')))
        if not(all(0 <= x <= 10**3 for x in citations)):
            print('Элементы массива выходят за пределы допустимого диапазона')
            exit()
        if len(citations) > 5000 :
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()

    # Замер времени
    start_time = time.time()

  
    h = h_index(citations)
    
    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task5/txtf/output.txt', 'w') as f:
        f.write(str(h))
    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")
