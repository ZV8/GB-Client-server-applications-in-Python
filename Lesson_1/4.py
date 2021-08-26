""" 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode). """


one = "разработка"
print(one)
one_bytes = one.encode('utf-8')
print(one_bytes)
dec_one_bytes = one_bytes.decode('utf-8')
print(dec_one_bytes)

print('-'*50)

two = "администрирование"
print(two)
two_bytes = two.encode('utf-8')
print(two_bytes)
dec_two_bytes = two_bytes.decode('utf-8')
print(dec_two_bytes)

print('-'*50)

three = "protocol"
print(three)
three_bytes = three.encode('utf-8')
print(three_bytes)
dec_three_bytes = three_bytes.decode('utf-8')
print(dec_three_bytes)

print('-'*50)

four = "standard"
print(four)
four_bytes = four.encode('utf-8')
print(four_bytes)
dec_four_bytes = four_bytes.decode('utf-8')
print(dec_four_bytes)
