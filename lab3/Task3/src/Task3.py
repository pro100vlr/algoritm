from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab3/task3"

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

   data = read_file_data(lab_task + input_path)
    
   n, k = data[0]
   arr = data[1]

   assert 1 <= n <= 10**5 and 1 <= k <= 10**5, "Выход за пределы значений для n и k"
   assert all(abs(element) <= 10**9 for element in arr), "Не все значения находятся в указанном диапазоне"

   result = can_sort_with_k_swaps(n, k, arr)

   write_data(lab_task + output_path, result)

   print_input_output(lab_task + input_path, result)

   measure(can_sort_with_k_swaps, n, k, arr)