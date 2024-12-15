from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab1/task5"

def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Обмен местами текущего элемента и минимального
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]
    
    assert (1<= n <= 10**3), "Выход за пределы значений для n"
    assert (all(abs(element) <= 10**9 for element in arr)), "Не все значения находятся в указанном диапазоне"
    
    result = ' '.join(map(str, selection_sort(arr, n)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(selection_sort, arr, n)
    