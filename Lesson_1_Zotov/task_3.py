"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение, придумайте как это сделать
"""


def check_ascii(item):
    try:
        item.encode("ascii")
    except UnicodeEncodeError as e:
        print(f'Error: {e}')
        print(f'Слово "{item}" невозможно записать в байтовом типе с помощью маркировки b''')


words = ['attribute', 'класс', 'функция', 'type']
for word in words:
    check_ascii(word)

words = [b'attribute', b'type']
for word in words:
    print(word)
    print(type(word))

# Ответ: слова «класс» и «функция» невозможно записать в байтовом типе с помощью маркировки b
# SyntaxError: bytes can only contain ASCII literal characters.
