# Задание №4 по выбору : `Наибольшая общая подпоследовательность двух последовательностей`

Студентка ИТМО, Просветова Валерия Дмитриевна

## Вариант 19

## Задание 

Вычислить длину самой длинной общей подпоследовательности из двух последовательностей.

Даны две последовательности A = (a1, a2, ..., an) и B = (b1, b2, ..., bm), найти длину их самой длинной общей подпоследовательности, т.е. наибольшее неотрицатеьное целое число p такое, что существуют индексы 1 ≤ i1 < i2 < ... < ip ≤ n и 1 ≤ j1 < j2 < ... < jp ≤ m такие, что ai1 = bj1, ..., aip = bjp.

• Формат ввода / входного файла (input.txt).

– Первая строка: n - длина первой последовательности.

– Вторая строка: a1, a2, ..., an через пробел.

– Третья строка: m - длина второй последовательности.

– Четвертая строка: b1, b2, ..., bm через пробел.

• Ограничения: 1 ≤ n, m ≤ 100; −109 < ai, bi < 10^9.

• Формат вывода / выходного файла (output.txt). Выведите число p.

## Input / Output 

| Input    | Output   |
|----------|----------|
| 3        | 2        |
| 2 7 5    |          |
| 2        |          |
| 2 5      |          |

| Input    | Output   |
|----------|----------|
| 1        | 0        |
| 7        |          |
| 4        |          |
| 1 2 34   |          |

| Input    | Output   |
|----------|----------|
| 4        | 2        |
| 2 7 8 3  |          |
| 4        |          |
| 5 2 8 7  |          |

## Ограничения по времени и памяти

- Ограничение по времени. 1сек.

## Запуск проекта

`git clone https://github.com/pro100vlr/algoritm.git`   
`python3 -m lab7.task4.src.task4`

### Запуск теста:   
   
`git clone https://github.com/pro100vlr/algoritm.git`   
`python3 -m lab7.task4.tests.test_task4`