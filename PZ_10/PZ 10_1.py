# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого максимального элемента:
# Произведение элементов средней трети:

import math
import random

try:
    n = int(input('Введите количество элементов: '))
except ValueError:
    print('Введите число.')
    exit()

nums = [random.randint(-100, 100) for i in range(n)]

with open('file1.txt', 'w', encoding='utf-8') as file:
    file.write(f'{nums}')

N = len(nums)
start = N // 3
end = (2 * N) // 3

sort_nums = nums.copy()
sort_nums.sort()

with open('file2.txt', 'w', encoding='utf-8') as file:
    file.write(
        f'Исходные данные: {nums}\n'
        f'Количество элементов: {len(nums)}\n'
        f'Индекс первого максимального элемента:  {nums.index(max(nums))}\n'
        f'Произведение элементов средней трети: {math.prod(sort_nums[start:end])}'
    )