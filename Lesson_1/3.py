""" 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. """


one = b"attribute"
print(one)
print(type(one))

two = b"класс"
print(two)
print(type(two))

three = b"функция"
print(three)
print(type(three))

four = b"type"
print(four)
print(type(four))


# Ответ: слова «класс» и «функция»
# SyntaxError: bytes can only contain ASCII literal characters.
