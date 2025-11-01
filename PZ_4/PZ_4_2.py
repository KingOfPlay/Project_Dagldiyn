#Дано целое число N(>1). Вывести наименьшее из целых чисел K,для
#которых сумма 1+2+...+K будет больше или равна N, и саму эту сумму.
try:
    N = int(input("Введите целое число N (>1): "))

    if N <= 1:
        print("Ошибка: N должно быть больше 1")
    else:
        K = 0
        total_sum = 0

        while total_sum < N:
            K += 1
            total_sum += K

        print(f"Наименьшее K: {K}")
        print(f"Сумма: {total_sum}")
except ValueError: print("Не то")