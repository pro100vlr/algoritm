def read_data(input_path, n_limit, element_limit):
    with open(input_path, 'r') as f:
        n = int(f.readline().strip())  
        array = list(map(int, f.readline().strip().split())) 
        if not(n >= 1 and n <= n_limit):
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()
        if not(all(abs(x) <= element_limit for x in array)):
            print('Элементы массива выходят за пределы допустимого диапазона')
            exit()  
    return n, array


input_path = '/txtf/input.txt'