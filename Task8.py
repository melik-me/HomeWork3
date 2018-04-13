# Задание 8

# Оформляем в функции наши задания на уроке:

# Пишем функцию, которая попросит пользователя ввести слово (строка
# без пробелов в середине, а вначале и в конце пробелы могут быть). Пока
# он не введёт правильно, просите его ввести. Функция возвращает
# введённое слово

def enter_sandman():
    while True:
        word = input("Enter a word: ").strip()
        if ' ' not in word:
            break
    return word

s = enter_sandman()
print(s)

# Пишем функцию, которая попросит ввести число. Пока он не введёт
# правильно, просите его ввести. Функция возвращает введённое число.

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

n = enter_aquaman()
print(n)
