def read_data(input_path):
    with open(input_path, 'r') as f:
        n = int(f.readline().strip())  # Первое число - количество элементов
        array = list(map(int, f.readline().strip().split()))  # Чтение массива
    return n, array

def write_data(output_path, res_array):
    with open(output_path, 'w') as f:
        f.write(' '.join(map(str, res_array)) + '\n')

input_path = '/txtf/input.txt'
output_path = '/txtf/output.txt'