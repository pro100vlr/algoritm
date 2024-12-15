from utils import read_file_data, input_path, output_path, print_input_output, write_data, measure

lab_task = "lab4/task4"

def check_brackets(sequence):
    stack = []
    # Словарь для соответствия закрывающих и открывающих скобок
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(sequence):
        # Если символ - открывающая скобка, добавляем её и её позицию в стек
        if char in "([{":
            stack.append((char, i + 1))  
        elif char in ")]}":
            # Если символ - закрывающая скобка
            if not stack:
                # Ошибка: лишняя закрывающая скобка
                return i + 1
            top, position = stack.pop()
            if top != matching_brackets[char]:
                # Ошибка: несоответствие закрывающей скобки
                return i + 1
    
    # Если после обхода строки в стеке остались открывающие скобки
    if stack:
        _, position = stack[0] 
        return position  # последняя незакрытая открывающая скобка
    
    return "Success"

if __name__ == "__main__":

    data = read_file_data(lab_task + input_path)
    
    sequence = data[0]

    assert 1 <= len(sequence) <= 10**5, "Cлишком длинная последовательность"

    result = str(check_brackets(sequence))
   
    write_data(lab_task + output_path, result)

    print_input_output(lab_task + input_path, result)

    measure(check_brackets, sequence)

