# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов.
data = open (r"numbers.txt", "r")
numbers = data.read()
data.close()
print(numbers)
list = []
for c in numbers:
    if c not in list:
        if numbers.count(c) == 1:
            list.append(int(c))
print(f"Список неповторяющихся элементов: {list}")