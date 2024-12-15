# Инициализация пустого стека
stack = None

# Функция проверки, пуст ли стек
def isEmpty(stack):
    return stack is None

# Функция добавления элемента (push)
def push(stack, value):
    return [value, stack]  # Создаем новый узел с текущим значением и ссылкой на старую вершину

# Функция удаления элемента (pop)
def pop(stack):
    if isEmpty(stack):
        raise IndexError("Pop from empty stack")
    value, stack = stack  # Возвращаем значение текущего элемента и переходим к следующему узлу
    return value, stack

# Функция отображения стека
def display(stack):
    current = stack
    while current:
        print(current[0], end=" -> ")
        current = current[1]
    print("None")

if __name__ == "__main__":
    # Пример использования
    stack = push(stack, 10)
    stack = push(stack, 20)
    stack = push(stack, 30)
    display(stack)  # Вывод: 30 -> 20 -> 10 -> None
    value, stack = pop(stack)
    print(value)  # Вывод: 30
    display(stack)  # Вывод: 20 -> 10 -> None

