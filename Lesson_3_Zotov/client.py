"""Программа-клиент"""

import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, ADDRESS, PORT
from common.utils import get_message, send_message


class Client():
    def __init__(self):
        '''Загружаем параметы коммандной строки'''
        # client.py 192.168.31.76 4321
        try:
            self.server_address = sys.argv[1]
            self.server_port = int(sys.argv[2])
            if self.server_port < 1024 or self.server_port > 65535:
                raise ValueError
        except IndexError:
            self.server_address = DEFAULT_IP_ADDRESS
            self.server_port = DEFAULT_PORT
        except ValueError:
            print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)

        # Инициализация сокета и обмен

        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.connect((self.server_address, self.server_port))
        self.message_to_server = self.create_presence()
        send_message(self.transport, self.message_to_server)
        try:
            self.answer = self.process_ans(get_message(self.transport))
            print(self.answer)
        except (ValueError, json.JSONDecodeError):
            print('Не удалось декодировать сообщение сервера.')

    def create_presence(self, account_name='Guest'):
        '''
        Функция генерирует запрос о присутствии клиента
        :param account_name:
        :return:
        '''
        # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
        self.out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            },
            ADDRESS: self.server_address,
            PORT: self.server_port
        }
        return self.out

    def process_ans(self, message):
        '''
        Функция разбирает ответ сервера
        :param message:
        :return:
        '''
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return f'200 : OK\nADDRESS : {message[ADDRESS]}\nPORT : {message[PORT]}'
            return f'400 : {message[ERROR]}'
        raise ValueError


if __name__ == '__main__':
    Client()
