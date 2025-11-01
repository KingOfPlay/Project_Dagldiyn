# Дано двухзначноечное число. Вывести число, полученное при перестановке цифр исходного числа
try:
    a = int(input('Введите двухзначное число: '));
    if 10 <= a <= 99:
        tens = a // 10
        units = a % 10
        result = units * 10 + tens
        print(f'Результат: {result}')
    else:
        print('Не двухзначное число')
except ValueError: print("Не то")