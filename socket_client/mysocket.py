import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 14200))
s.listen()
while True:

#Waiting For a Connection
    connection, client = s.accept()

    print(client, 'Connected')

    data = connection.recv(512)

    print('Received "' + data.decode() + '"')
    connection.send("OK".encode())

    connection.close()
