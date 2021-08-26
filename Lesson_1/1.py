""" 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode 
и также проверить тип и содержимое переменных. """

print('Строки:')
one = "разработка"
print(one)
print(type(one))

two = "сокет"
print(two)
print(type(two))

three = "декоратор"
print(three)
print(type(three))

print('\nUnicode:')
one = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
print(one)
print(type(one))

two = "\u0441\u043e\u043a\u0435\u0442"
print(two)
print(type(two))

three = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
print(three)
print(type(three))
