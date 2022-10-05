# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
N = int (input('Bведите число (размер списка) > 0: '))
from fileinput import close
import random
if N > 0:
    list = []
    list2 = [] 
    for i in range(N):
        a = round(random.random() * 10, 2)
        list.append(a)
    else:
        print(f"Сгенерированный массив длинной {N}: {list}")
        if N != 1:
            list2 = []
            for k in range(len(list)):
                list2.append(list[k] - int(list[k]))
                difference = round(max(list2) - min(list2), 2)
            else:
                print(f"Разница между максимальным и минимальным значением дробной части сгенерированного массива:\n{difference}")
        else:
            print("В списке нет второго элемента!")
else:
    print("Ошибка ввода!")