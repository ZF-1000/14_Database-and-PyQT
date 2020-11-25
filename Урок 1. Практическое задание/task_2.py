"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping():
    while True:
        start_ip = input('Введите первоначальный адрес: ')   # запрос первоначального адреса
        try:
            last_oct = int(start_ip.split('.')[3])  # последний октет
            break
        except Exception as e:
            print(e)
    while True:
        count_ip = input('Сколько адресов проверить?: ')
        if not count_ip.isnumeric():
            print('Необходимо ввести число: ')
        else:
            if (last_oct + int(count_ip)) > 254:
                print(f'Можем менять только последний октет, т.е.'
                      f'максимальное число хостов для проверки: {254 - last_oct}')
            else:
                break

    host_list = []
    [host_list.append(str(ip_address(start_ip) + x)) for x in range(int(count_ip))]     # список ip адресов
    return host_ping(host_list)     # передаём список ip адресов в функцию для проверки доступности из task_1


if __name__ == '__main__':
    host_range_ping()
