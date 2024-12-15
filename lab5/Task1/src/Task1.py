from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab5/task1"
def is_heap(n, array):
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Проверяем левый потомок
        if left < n and array[i] > array[left]:
            return "NO"
        
        # Проверяем правый потомок
        if right < n and array[i] > array[right]:
            return "NO"
    
    return "YES"

if __name__ == "__main__":
           
    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    array = data[1]

    assert (1 <= n <= 10**6), "Выход за пределы значений для n"
    assert all(abs(element) <= 2*10**9 for element in array), "Не все значения находятся в указанном диапазоне"

    result = is_heap(n, array)
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(is_heap, n, array)

    result = is_heap(n, array)