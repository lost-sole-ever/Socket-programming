import socket

HOST_NAME = socket.gethostname()
host = socket.gethostbyname(HOST_NAME)
port = 9000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"message from client is {message}")
    communication_socket.send(f"got your message! Thank you!!".encode("utf-8"))
    communication_socket.close()
    print(f"connection with {address} ended!")
