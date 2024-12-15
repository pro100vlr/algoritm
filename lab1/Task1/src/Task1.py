from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab1/task1"

def insertion_sort(arr, n):
    # Реализация алгоритма сортировки вставками
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    n = data[0]
    arr = data[1]
    
    assert (1<= n <= 10**3), "Выход за пределы значений для n"
    assert (all(abs(element) <= 10**9 for element in arr)), "Не все значения находятся в указанном диапазоне"

    result = ' '.join(map(str, insertion_sort(arr, n)))
    
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(insertion_sort, arr, n)


