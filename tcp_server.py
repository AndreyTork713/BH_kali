import socket
import threading

IP = '0.0.0.0'

PORT = 9998

def main():
    # Создаём объект сервер
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Передаем IP-адрес и порт, который должен прослушивать наш сервер
    server.bind((IP, PORT))
    # Просим сервер слушать, отложенных соединений
    # должно быть не больше пяти
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    # Главный цикл сервера, где он ждет соединения
    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client,
                                          args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()


