import socket

host = "10.2.96.187"
port = 9000

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))

socket.send(f"Hello World!!".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))