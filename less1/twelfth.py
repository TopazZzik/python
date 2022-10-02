N = int (input('Bведите число > 0: '))
import random
list = []
indexes = []
if N > 0:
    for i in range(N):
        list.append(i)
    else:
        print(f"Исходный список: {list}")
        newList = [None] * N
        for i in range(N):
            k = random.randint(0,N-1)
            while k in indexes:
                k = random.randint(0,N-1)
            else:
                indexes.append(k)
                newList[k] = list[i]
        else:
            print(f"Перемешанный список: {newList}") 
else:
    print("Ошибка ввода!")