# Задание №2 по варианту  : `Анти-quick sort`
Студентка ИТМО, Просветова Валерия Дмитриевна

## Вариант 19

## Задание 

Для сортировки последовательности чисел широко используется быстрая сортировка - QuickSort. Далее приведена программа на языке Pascal Python, которая сортирует массив a, используя этот алгоритм.

`def qsort (left, right):
        key = a [(left + right) // 2]
        i = left
        j = right
while i <= j:
        while a[i] < key: # first while
                i += 1
        while a[j] > key : # second while
                j -= 1
        if i <= j :
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
if left < j:
        qsort(left, j)
if i < right:
        qsort(i, right)
qsort(0, n - 1)`

Хотя QuickSort является очень быстрой сортировкой в среднем, существуют тесты, на которых она работает очень долго. Оценивать время работы алгоритма
будем числом сравнений с элементами массива (то есть, суммарным числом сравнений в первом и втором while). Требуется написать программу, генерирующую тест, на котором быстрая сортировка сделает наибольшее число таких сравнений. Задача на acmp.

• Формат входного файла (input.txt). В первой строке находится единственное число n (1 ≤ n ≤ 10^6).

• Формат выходного файла (output.txt). Вывести перестановку чисел от 1 до n, на которой быстрая сортировка выполнит максимальное число сравнений.Если таких перестановок несколько, вывести любую из них.

## Input / Output 

| Input    | Output   |
|----------|----------|
| 3        | 1 3 2    |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта

`git clone https://github.com/pro100vlr/algoritm.git`   
`cd algoritm/lab3/`  
`python3 -m Task2.src.Task2`   

### Запуск теста:   
   
`git clone https://github.com/pro100vlr/algoritm.git`   
`cd algoritm/lab3/`  
`python -m Task2.tests.test_task2`