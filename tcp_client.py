import socket

target_host = 'www.google.com'
target_port = 80

# Создаем объект сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем клиент
client.connect((target_host, target_port))

# Отправляем какие-нибудь данные
client.send(b"GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Принимаем какие-нибудь данные
response = client.recv(4096)

print(response.decode())
client.close()