# Задание 4

# У вас есть список чисел.

# Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым

from copy import deepcopy

l = list()
# i = 0
#
# while True:
#     l.append(input("Please enter an element of a list (It should be a number) or press Enter to finish:\n"))
#     if len(l[-1]) == 0:
#         l.remove('')
#         break
#     l[i] = int(l[i])
#     i += 1

while True:
    s = input("Please enter an element of a list (It should be a number) or press Enter to finish:\n")
    if len(s) == 0:
        break
    l.append(int(s))

l2 = deepcopy(l)

print('This is your list:', l)

while l:
    print(l.pop(0))
    print(l)

# ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
# «удаляет» первый символ строки, пока она не станет пустой?

s = input("Please enter a string:\n")

while s:
    print(s[0])
    s = s[1:]
    print(s)

# Напишите цикл, который выводит на экран и удаляет элементы списка от самого
# маленького до самого большого, пока он не останется пустым.

l3 = deepcopy(l2)

l2.sort()

print(l3)

while l3:
    print(l2[0])
    l3.remove(l2[0])
    print(l3)
    l2.pop(0)
