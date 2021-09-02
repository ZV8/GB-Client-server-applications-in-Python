"""Программа-сервер"""

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, ADDRESS, PORT
from common.utils import get_message, send_message


class Server():
    def __init__(self):
        '''
        Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
        Сначала обрабатываем порт:
        server.py -p 4321 -a 192.168.31.76
        :return:
        '''

        try:
            if '-p' in sys.argv:
                self.listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            else:
                self.listen_port = DEFAULT_PORT
            if self.listen_port < 1024 or self.listen_port > 65535:
                raise ValueError
        except IndexError:
            print('После параметра -\'p\' необходимо указать номер порта.')
            sys.exit(1)
        except ValueError:
            print(
                'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)

        # Затем загружаем какой адрес слушать

        try:
            if '-a' in sys.argv:
                self.listen_address = sys.argv[sys.argv.index('-a') + 1]
            else:
                self.listen_address = ''

        except IndexError:
            print(
                'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)

        # Готовим сокет

        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.bind((self.listen_address, self.listen_port))

        # Слушаем порт

        self.transport.listen(MAX_CONNECTIONS)

        while True:
            self.client, self.client_address = self.transport.accept()
            try:
                self.message_from_cient = get_message(self.client)
                print(self.message_from_cient)
                # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
                self.response = self.process_client_message(self.message_from_cient)
                send_message(self.client, self.response)
                self.client.close()
            except (ValueError, json.JSONDecodeError):
                print('Принято некорретное сообщение от клиента.')
                self.client.close()

    def process_client_message(self, message):
        '''
        Обработчик сообщений от клиентов, принимает словарь -
        сообщение от клинта, проверяет корректность,
        возвращает словарь-ответ для клиента

        :param message:
        :return:
        '''
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {
                RESPONSE: 200,
                ADDRESS: self.listen_address,
                PORT: self.listen_port
            }
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }


if __name__ == '__main__':
    Server()
