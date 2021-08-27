"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

resources = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for args in resources:
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for i, line in enumerate(subproc_ping.stdout):
        result = chardet.detect(line)
        dec_line = line.decode(result['encoding'])
        print(dec_line)
        if i == 5:
            break
