def read_data(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        if not(1<=n<=10**6):
            print("Количество элементов в массиве не соответствует требованиям") 
            exit() 
        commands = [line.strip() for line in lines[1:n+1]]

    return n, commands


def write_data(output_path, res_array):
    with open(output_path, 'w') as file:
        for value in res_array:
            file.write(f"{value}\n")

input_path = '/txtf/input.txt'
output_path = '/txtf/output.txt'