# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xyz = ["X", "Y", "Z"]
a = []
for i in range(3):
    a.append(input(f"Введите значение {xyz[i]}: "))
left = not (a[0] or a[1] or a[2])
right = not a[0] and not a[1] and not a[2]
result = left == right
if result == True:
    print("Утверждение истинно!")
else:
    print("Утверждение ложно!")