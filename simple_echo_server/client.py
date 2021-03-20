import socket

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 9090))
print('Вы подключены к серверу.')

while True:
    msg = input('Введите ваше сообщение: ')

    if msg == 'exit':
        sock.close()
        print('Вы отключены от сервера.')
        break

    sock.send(msg.encode())
    print('Сообщение отправлено на сервер.')

    data = sock.recv(1024)
    print('Сообщение, полученное от сервера:')

    print(data.decode())
