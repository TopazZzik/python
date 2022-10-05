# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
N = int (input('Bведите число > 0, для которого необходимо вывести список чисел Негофибоначчи и Фибоначчи: '))
if N > 0:
    def fibonacci(N):
        a, b = 0, 1
        for i in range(N+1):
            yield a
            a, b = b, a + b
    data = list(fibonacci(N))
    def fibonacci(N):
        a, b = -1, -1
        for i in range(N):
            yield a
            a, b = b, a + b
    data1 = list(fibonacci(N))
    data2 = data1[::-1]
    print("Cписок чисел Негофибоначчи и Фибоначчи: ")
    res = data2 + data
    for i in range(0, len(res)):
            if i == len(res)-1:
                print(res[i])
            else:
                print(res[i], end=", ")
else:
    print("Ошибка ввода!")