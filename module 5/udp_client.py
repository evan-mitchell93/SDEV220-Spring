import socket

#ip and port we want to send data to
serv_addr = ('localhost',6789)

max_size = 1024

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto("Hi I'm the client sending data".encode('utf-8'),serv_addr)

data,server = client.recvfrom(max_size)
print("The server responded with: ", data)
client.close()