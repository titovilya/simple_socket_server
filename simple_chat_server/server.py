import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9090))

clients = {}

while True:
    message, address = server_socket.recvfrom(1024)

    print(message.decode())

    message = json.loads(message.decode())

    clients.setdefault(address, message['username'])

    new_message = json.dumps({'username': clients[address], 'message': message['message']})

    for client_addr in clients:
        server_socket.sendto(str(new_message).encode(), client_addr)

