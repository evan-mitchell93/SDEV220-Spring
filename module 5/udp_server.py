import socket

#server code for UDP

serv_addr = ('localhost',6789)
max_size = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(serv_addr)

data,client = server.recvfrom(max_size)

print("Client sent: ",data)
server.sendto("Hello I'm server".encode('utf-8'),client)
server.close()