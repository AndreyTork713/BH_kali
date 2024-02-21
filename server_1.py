from socket import *
import threading

host = 'localhost'
port = 777
addr = (host, port)


    # Создаём объект сервер
tcp_socket = socket(AF_INET, SOCK_STREAM)
# Передаем IP-адрес и порт, который должен прослушивать наш сервер
tcp_socket.bind(addr)
# Просим сервер слушать, отложенных соединений
# должно быть не больше пяти
tcp_socket.listen(1)
print(f'[*] Listening on {host}:{port}')

    # Главный цикл сервера, где он ждет соединения
while True:
    question = input('Хотите выйти?: y/n')
    if question == 'y': break

    print('Ожидайте соединения...')
    client, address = tcp_socket.accept()
    print(f'[*] Accepted connection from {addr}')
    data = client.recv(1024)
    if not data:
        client.close()
        break
    else:
        print(data)
        client.send(b'Hello from server!')
        client.close()

tcp_socket.close()

