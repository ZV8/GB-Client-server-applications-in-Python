""" 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в
строковый тип на кириллице. """

import subprocess
import chardet

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for i, line in enumerate(subproc_ping.stdout):
    result = chardet.detect(line)
    dec_line = line.decode(result['encoding'])
    print(dec_line)
    if i == 5:
        break

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for i, line in enumerate(subproc_ping.stdout):
    result = chardet.detect(line)
    dec_line = line.decode(result['encoding'])
    print(dec_line)
    if i == 5:
        break
