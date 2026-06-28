# В матрице найти максимальный положительный элемент, кратный 4.

import random
from functools import reduce

n = int(input('Введите длину матрицы: '))
m = int(input('Введите ширину матрицы: '))

matrix = [[random.randint(10, 99) for j in range(n)] for i in range(m)]

print("\nИсходная матрица:")
list(map(print, matrix))

flat_matrix = reduce(lambda a, row: a + row, matrix, [])

filtered_elements = list(filter(lambda x: x > 0 and x % 4 == 0, flat_matrix))

if filtered_elements:
    max_element = reduce(lambda a, b: a if a > b else b, filtered_elements)
    print(f"\nМаксимальный положительный элемент, кратный 4: {max_element}")
else:
    print("\nВ матрице нет положительных элементов, кратных 4")