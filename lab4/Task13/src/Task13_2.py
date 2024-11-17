# Инициализация пустой очереди
head = None
tail = None
size = 0
max_size = 3  # Максимальный размер очереди 

# Функция проверки, пуста ли очередь
def isEmpty(head):
    return head is None

# Функция проверки, полна ли очередь
def isFull(size, max_size):
    return size >= max_size

# Функция добавления элемента (enqueue)
def enqueue(head, tail, size, value):
    if isFull(size, max_size):
        raise OverflowError("Queue is full")
    new_node = [value, None]  # Новый узел
    if tail:  # Если очередь не пуста
        tail[1] = new_node  # Устанавливаем связь с новым узлом
    tail = new_node
    if head is None:  # Если очередь пуста, новый узел — это и начало, и конец
        head = tail
    size += 1
    return head, tail, size

# Функция удаления элемента (dequeue)
def dequeue(head, tail, size):
    if isEmpty(head):
        raise IndexError("Dequeue from empty queue")
    value, head = head  # Сдвигаем указатель начала
    if head is None:  # Если очередь опустела
        tail = None
    size -= 1
    return value, head, tail, size

# Функция отображения очереди
def display(head):
    current = head
    while current:
        print(current[0], end=" -> ")
        current = current[1]
    print("None")

# Пример использования
head, tail, size = enqueue(head, tail, size, 10)
head, tail, size = enqueue(head, tail, size, 20)
head, tail, size = enqueue(head, tail, size, 30)
display(head)  # Вывод: 10 -> 20 -> 30 -> None
value, head, tail, size = dequeue(head, tail, size)
print(value)  # Вывод: 10
display(head)  # Вывод: 20 -> 30 -> None
head, tail, size = enqueue(head, tail, size, 40)
display(head)  # Вывод: 20 -> 30 -> 40 -> None