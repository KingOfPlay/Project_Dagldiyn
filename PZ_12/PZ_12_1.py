# Для каждой строки матрицы с нечетным номером найти среднее
# арифметическое ее элементов.


import random

n = int(input('Введите длину матрицы: '))
m = int(input('Введите ширину матрицы: '))

matrix = [[random.randint(10,99) for j in range(n)] for i in range(m)]
for i in range(m):
    print(matrix[i])

for row in matrix:
    print(" ".join(f"{num:4}" for num in row))

row_averages = [
    (i + 1, sum(row) / len(row))
    for i, row in enumerate(matrix)
    if (i + 1) % 2 != 0
]

for row_num, avg in row_averages:
    print(f"Строка №{row_num}: среднее арифметическое элементов = {avg:.2f}")
