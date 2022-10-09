# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
#многочлена и записать в файл многочлен степени k
#k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
#Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
import random
k = int (input('Задайте степень многочлена (введите целое число) > 0: '))
if k > 0:
    my_string = ""
    while k >= 0:
        r = random.randint(-1,1)
        if r>0:
            if my_string != "":
                my_string += " + "
            if k > 1:
                my_string += str(r) + "x^" + str(k) 
            elif k==1:
               my_string += str(r) + "x"
            else:
                my_string += str(r)
        elif r<0:
            my_string += " - "
            if k > 1:
                my_string +=  str(abs(r)) + "x^" + str(k)
            elif k==1:
               my_string += str(abs(r)) + "x" 
            else:
                my_string +=  str(abs(r))
        k = k-1
    else:
        my_string += " = 0"
        data = open (r"equation.txt", "w")
        data.write(my_string)
        data.close()  
else:
    print("Ошибка ввода!")