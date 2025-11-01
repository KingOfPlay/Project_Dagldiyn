#Дано вещественное число и целое число N(>0)
#Найти А в степени N: A**N = АА ... * А (числа А перемножаются N раз)
try:
    a = float(input('Введите вещественное число: '))
    N = int(input('Введите целое число: '))
    if N > 0:
        A = 1
        c = 0
        while c != N:
            A *= a
            c += 1
        print(A)
    else:
        print('N<0')
except ValueError: print("Не то")
