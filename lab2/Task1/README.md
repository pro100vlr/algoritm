# Задание №1 по варианту  : `Сортировка слиянием`
Студентка ИТМО, Просветова Валерия Дмитриевна

## Вариант 19

## Задание 

1.Используя псевдокод процедур Merge и Merge-sort из презентации к Лекции 2 (страницы 6-7), напишите программу сортировки слиянием на Python и проверьте сортировку, создав несколько рандомных массивов, подходящих под параметры:

• Формат входного файла (input.txt). В первой строке входного файла содержится число n (1 ≤ n ≤ 2 · 10^4) — число элементов в массиве.
Во второй строке находятся n различных целых чисел, по модулю не превосходящих 10^9.

• Формат выходного файла (output.txt). Одна строка выходного файла с отсортированным массивом. Между любыми двумя числами должен
стоять ровно один пробел.

2.Для проверки можно выбрать наихудший случай, когда сортируется массив размера 1000, 10^4, 10^5 чисел порядка 10^9, отсортированных в обратном
порядке; наилучший, когда массив уже отсортирован, и средний. Сравните, например, с сортировкой вставкой на этих же данных.

3.Перепишите процедуру Merge так, чтобы в ней не использовались сигнальные значения. Сигналом к остановке должен служить тот факт, что все элементы массива L или R скопированы обратно в массив A, после чего в этот массив копируются элементы, оставшиеся в непустом массиве.
или перепишите процедуру Merge (и, соответственно, Merge-sort) так, чтобы в ней не использовались значения границ и середины - p, r и q

## Input / Output 

| Input            | Output             |
|------------------|--------------------|
| 6                | 26 31 41 41 58 59  |
| 31 41 59 26 41 58|                    |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта

`git clone https://github.com/pro100vlr/algoritm.git`   
`cd algoritm/lab2/`  
`python3 -m Task1.src.Task1`   
   
### Запуск теста:   
   
`git clone https://github.com/pro100vlr/algoritm.git`   
`cd algoritm/lab2/`  
`python -m Task1.tests.test_task1` 
   