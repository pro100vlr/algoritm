import psutil
import time

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

    # Измеряем память
    mem_before = psutil.Process().memory_info().rss

    # Чтение данных из файла
    with open("Task8/txtf/input.txt", "r") as file:
        n = int(file.readline().strip())
        if not(1 <= n <= 10**6):
            print("Количество элементов в массиве выходит за пределы допустимого диапазона")
            exit()
        expression = file.readline().strip().split()

   # Замер времени
    start_time = time.time()

    result = evaluate_postfix(expression)

    end_time = time.time()
    mem_after = psutil.Process().memory_info().rss

    # Запись результата в файл
    with open("Task8/txtf/output.txt", "w") as file:
        file.write(str(result))

    print(f"Время работы: {end_time - start_time :.3f} с, Память - {(mem_after - mem_before) / 1024**2 :.3f} Мб")