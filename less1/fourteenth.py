# Напишите программу, которая найдёт произведение пар чисел списка (cписок создаем как в предыдущем задании). Парой считаем первый и последний элемент, второй и предпоследний и т.д..
from math import prod
N = int (input('Bведите число (размер списка) > 0: '))
if N > 0:
    import random
    list = random.sample(range(10), N)
    print(f"Сгенерированный список: {list}")
    if N == 1:
        print("В списке нет второго элемента!")
    else:
        chet = 1
        list = []
        middle = 0
    if N%2 != 0:
        chet = 0
        middle = round(N/2) + 1
    else:
        middle = round(N/2)
    list1 = []
    for i in range(middle):
        if chet !=1 and i == middle:
            list1.append(list[i]^2)
        else:
            list1.append(list[i]*list[N-1-i])
    print(f'Произведение элементов списка: {list1}')
else:
    print(f"Ошибка ввода!")