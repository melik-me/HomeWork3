# Задание 2

# Пользователь вводит строку. Разрежьте её на две равные части (если длина строки —
# чётная, а если длина строки нечётная, то длина первой части должна быть на один
# символ больше). Переставьте эти две части местами, результат запишите в новую
# строку и выведите на экран.

s1 = input("Please enter a string:\n")

if len(s1) % 2 == 0:
    i = int(len(s1) / 2)
else:
    i = len(s1) // 2 + 1

s2 = s1[i:len(s1)] + s1[0:i]

print(s2)
