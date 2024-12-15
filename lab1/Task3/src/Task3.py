from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab1/task3"

def insertion_sort_descending(arr, n):

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Вставляем элемент на его место, используя swap
        # Будем делать swap, пока не найдем правильную позицию для key
        while j >= 0 and arr[j] < key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]  # Обмениваем элементы (swap)
            j -= 1
    
    return arr

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]

    assert (1<= n <= 10**3), "Выход за пределы значений для n"
    assert (all(abs(element) <= 10**9 for element in arr)), "Не все значения находятся в указанном диапазоне"
    
    result = ' '.join(map(str, insertion_sort_descending(arr, n)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(insertion_sort_descending, arr, n)