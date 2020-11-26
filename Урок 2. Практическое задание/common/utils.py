from common.variables import *
from errors import IncorrectDataRecivedError, NonDictInputError
import json
import sys
sys.path.append('../')
from decos import log


# Утилита приёма и декодирования сообщения
# принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку значения
@log
def get_message(client_sock):
    encoded_response = client_sock.recv(MAX_PACKAGE_LENGTH)  # recv — получить данные. На входе байты
    # isinstance - возвращает флаг, указывающий на то, является ли указанный объект
    # экземпляром указанного класса
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)   # из байтов получаем json объект
        # json.loads() - метод считывает строку в формате JSON и возвращает объекты Python
        response = json.loads(json_response)    # распарсили словарь
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


# Утилита кодирования и отправки сообщения. Принимает словарь и отправляет его
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    json_message = json.dumps(message)    # json.dumps() - метод возвращает строку в формате JSON
    encoded_message = json_message.encode(ENCODING)   # из json объекта получаем байты
    sock.send(encoded_message)          # байты шлём по сети
