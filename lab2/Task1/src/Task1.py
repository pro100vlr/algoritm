from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab2/task1"

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Сортируем левую и правую части
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Процедура слияния без использования сигнальных значений
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы из L (если есть)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы из R (если есть)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Чтение данных из файла input.txt

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    arr = data[1]

    assert (1<= n <= 2*10**4), "Выход за пределы значений для n"
    assert all(abs(element) <= 10**9 for element in arr), "Не все значения находятся в указанном диапазоне"
    
    result = ' '.join(map(str, merge_sort(arr)))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(merge_sort, arr)