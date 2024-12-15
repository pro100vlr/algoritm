from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab3/task2"

def anti_quick_sort(n):    
    arr = list(range(1, n + 1))
    for i in range(2, n): 
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
    return arr
# Чтение данных из файла input.txt

if __name__ == "__main__":
  
    data = read_file_data(lab_task + input_path)
    
    n = data[0]

    assert 1 <= n <= 10**6, "Выход за пределы значений для n"
    
    result = ' '.join(map(str, anti_quick_sort(n)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(anti_quick_sort, n)
    