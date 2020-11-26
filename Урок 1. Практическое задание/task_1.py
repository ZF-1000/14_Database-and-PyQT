"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться
доступность сетевых узлов. Аргументом функции является список, в котором каждый
сетевой узел должен быть представлен именем хоста или ip-адресом. В функции необходимо
перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
с помощью функции ip_address().
"""

'''
-w интервал
Определяет в миллисекундах время ожидания получения сообщения с эхо-ответом,
которое соответствует сообщению с эхо-запросом. Если сообщение с эхо-ответом
не получено в пределах заданного интервала, то выдаёт сообщение об ошибке 
"Request timed out". Интервал по умолчанию равен 4000 (4 сек)

-n счетчик
Задаёт число отправляемых сообщений с эхо-запросом. По умолчанию - 4.
'''

from subprocess import Popen, PIPE
from ipaddress import ip_address
import socket
from pprint import pprint


def host_ping(list_ip_addr, timeout=500, requests=1):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}    # словарь с результатами
    for addr in list_ip_addr:
        try:
            addr = ip_address(addr)
        except ValueError:
            addr = socket.gethostbyname(addr)
            # pass
        proc = Popen(f'ping {addr} -w {timeout} -n {requests}', shell=False, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:    # код завершения процесса
            results['Доступные узлы'] += f'{str(addr)}\n'
            res_str = f'{addr} - Узел доступен'
        else:
            results['Недоступные узлы'] += f'{str(addr)}\n'
            res_str = f'{addr} - Узел недоступен'
        print(res_str)
    return results


if __name__ == '__main__':
    list_ip_addresses = ['yandex.ru', '2.2.2.2', '192.168.0.111', '192.168.0.112']
    host_ping(list_ip_addresses)
