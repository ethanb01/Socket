import socket


print("trying to socket")
server_socket = socket.socket()
server_socket.bind(('', 5566))
print("server demareeeeee")

server_socket.listen()

print("a l ecouteeeeee")
connected_socket , address = server_socket.accept()
print("client conecteeeeeeee")

name_client = connected_socket.recv(1024)
name_client = name_client.decode("utf8")
print("Client name : %s" % name_client)

message = "Hello " + name_client
message = message.encode("utf8")

connected_socket.send(message)


connected_socket.close()
server_socket.close()