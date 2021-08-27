"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    print(word)
    word_bytes = word.encode('utf-8')
    print(word_bytes)
    dec_word_bytes = word_bytes.decode('utf-8')
    print(dec_word_bytes)
    print('-' * 50)
