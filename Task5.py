# Задание 5

# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
# (Football Coach)

# Посчитайте сколько слов в тексте (разбейте на слова методом строк split)

s = ("""We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
(Football Coach)""")

s = s.replace('\n', ' ')

l = s.split(' ')

print(len(l))

# Удалите знаки препинания (пройдитесь циклом все слова и удалите
# методом strip знаки препинания)

for i in range(len(l)):
    l[i] = l[i].strip(",.!?:-—;()\n")

print(l)

# Выведите слова в алфавитном порядке (найдите метод списка, который
# сортирует)

for i in range(len(l)):
    l[i] = l[i].lower()

l.sort()
print(l)

# Усложнённое ** (можно сначала его не делать):
# Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем
# количество «встречаний» этого слова)

d = dict()

# while len(l) > 0:
#     n = l.count(l[0])
#     d[l[0]] = n
#     s = l[0]
#     for i in range(n, 0, -1):
#         l.remove(s)

for word in l:
    n = l.count(word)
    d[word] = n

print(d)
