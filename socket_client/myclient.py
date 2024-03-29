import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting
#server.connect(("data.pr4e.org", 80))
#cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()


server.connect(("google.com", 80))
cmd='GET http://google.com HTTP/1.0\n\n'.encode()

server.send(cmd)


message = ["Hello","my","name","is","zeinab"]
for m in message:
    #server.sendall(m.encode())
    data = server.recv(1024)
    if(len(data)<1):
        break
    print('\n recive',repr(data).rstrip())

server.close()
#Connection Closed
