# Задания 9

# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию
# distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2,
# y2).
# Считайте четыре действительных числа от пользователя и выведите результат
# работы этой функции.

def enter_aquaman():
    while True:
        number = input("Enter a number: ")
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            break

    return number

def distance(x1, y1, x2, y2):
    dst = ((x2 -x1)**2 + (y2 -y1)**2)**0.5
    return dst

a = enter_aquaman()
b = enter_aquaman()
c = enter_aquaman()
d = enter_aquaman()
dstnc = distance(a, b, c, d)
print(dstnc)
