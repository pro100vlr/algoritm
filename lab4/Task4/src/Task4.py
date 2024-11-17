import psutil
import time

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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    with open('Task4/txtf/input.txt', 'r') as file:
        sequence = file.readline().strip()
        if not(1 <= len(sequence) <= 10**5):
            print('Количество элементов в массиве выходит за пределы допустимого диапазона')
            exit()

    # Замер времени
    start_time = time.time()

    result = check_brackets(sequence)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    with open('Task4/txtf/output.txt', 'w') as file:
        file.write(str(result) + "\n")

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")

