from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab1/task6"

def bubble_sort(arr, n):
    for i in range(n - 1): # количество итераций должно быть на 1 меньше
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Проверка корректности: массив должен быть отсортирован по возрастанию
def is_sorted(sorted_arr):
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] > sorted_arr[i + 1]:
            return False
    return True

if __name__ == '__main__':


    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]
    
    result = ' '.join(map(str, bubble_sort(arr, n)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(bubble_sort, arr, n)

