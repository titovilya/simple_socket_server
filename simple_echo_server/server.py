import socket

sock = socket.socket()
sock.bind(('', 9090))
print('Server started')

sock.listen(1)
print('Port listening')


while True:
    conn, addr = sock.accept()
    print('Пользователь присоединился.')
    print(addr)
    while True:
        data = conn.recv(1024)

        if not data:
            break

        print('Сообщение от пользователя:')

        msg = data.decode()
        conn.send(data)

        print(msg)
