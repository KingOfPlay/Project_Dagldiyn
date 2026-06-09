#Проверить есть ли в последовательности целых N чисел число K
import random

try:
    n = int(input('Введите количество элементов: '))
except ValueError:
    print('Введите число.')
    exit()

N = [random.randint(-100, 100) for i in range(n)]
print(N)

#N = list(input('Введите последовательность целых чисел: '))
#N = map(int, N)
K = int(input('Введите число:'));

print(list(filter(lambda x: x == K, N)))