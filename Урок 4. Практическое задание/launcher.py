"""Лаунчер"""

import subprocess

process = []

while True:
    action = input('Выберите действие: '
                   'q - выход, '
                   's - запустить сервер и клиенты, '
                   'x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':
        # Popen - выполняет дочернюю программу в новом процессе (не дожидается конца выполнения
        # вызванного процесса в отличие от метода call)
        # creationflags=None - один или несколько констант Windows
        # subprocess.CREATE_NEW_CONSOLE: Новый процесс имеет новую консоль вместо того,
        # чтобы наследовать консоль своего родителя (по умолчанию).
        # два типа скриптов: 1- на чтение, 2-ой на запись
        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        # Запускаем сервер!
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        # Запускаем клиентов:
        for i in range(clients_count):
            process.append(subprocess.Popen(f'python client.py -n test{i + 1}',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        while process:
            process.pop().kill()
