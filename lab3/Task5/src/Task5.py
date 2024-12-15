from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab3/task5"
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

    data = read_file_data(lab_task + input_path)
    
    citations = list(map(int,data[0].split(',')))

    assert all(0 <= num <= 1000 for num in citations), "Выход за пределы значений для citations"
    
    result = str(h_index(citations))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(h_index,citations)






