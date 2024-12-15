from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab4/task8"

def evaluate_postfix(expression):
    stack = []
    
    for token in expression:
        if token.isdigit():  # Если это число
            stack.append(int(token))
        else:  # Если это оператор
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    return stack[0]  # В стеке останется результат


if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    n = data[0]
    expression = data[1].split()
    
    assert (1 <= n <= 10**6), "Выход за пределы значений для n"

    result = str(evaluate_postfix(expression))

    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(evaluate_postfix, expression)


   