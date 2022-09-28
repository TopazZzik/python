# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.
N = int (input('Bведите число N > 0: '))
if N > 0:
    for i in range(-N, N + 1):
        if i == N:
            print(i)
        else:
            print(i, end=', ')
else:
    print("Ошибка ввода!")