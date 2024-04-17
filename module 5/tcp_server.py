import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))

    #TCP socket listens for connection requests
    server.listen()

    #block until a connection is established
    #conn socket object, addr client ip and port
    conn,addr = server.accept()

    with conn:
        print(f"Client info: {addr}")
        while True:
            data = conn.recv(1024)
            print(f"{data}")
            if not data:
                break

            conn.send(data)