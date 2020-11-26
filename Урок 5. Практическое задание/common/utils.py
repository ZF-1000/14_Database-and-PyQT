import json
import sys
sys.path.append('../')
from common.decos import log
from common.variables import *


# Утилита приёма и декодирования сообщения
# принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку значения
@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)  # recv — получить данные. На входе байты
    # isinstance - возвращает флаг, указывающий на то, является ли указанный объект
    # экземпляром указанного класса
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


# Утилита кодирования и отправки сообщения. Принимает словарь и отправляет его
@log
def send_message(sock, message):
    json_message = json.dumps(message)    # json.dumps() - метод возвращает строку в формате JSON
    encoded_message = json_message.encode(ENCODING)   # из json объекта получаем байты
    sock.send(encoded_message)          # байты шлём по сети
