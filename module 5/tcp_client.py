import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    #ask to connect to server
    client.connect((SERVER_HOST,SERVER_PORT))

    msg = input("Enter message: ")
    while msg != "QUIT":
        client.send(str.encode(msg))
        data = client.recv(1024)
        print(f"Server responded: {data}")
        msg = input("Enter message: ")
        
        