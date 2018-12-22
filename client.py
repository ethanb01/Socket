import socket


host,port = ('localhost' , 5566)

client_socket = socket.socket()
client_socket.connect((host,port))

name_client = input("Your name : ")
name_client = name_client.encode("utf8")
client_socket.sendall(name_client)


message = client_socket.recv(1024)
message = message.decode("utf8")
print(message)
client_socket.close()