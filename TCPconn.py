import socket

target_host = input("Host: ")
target_port = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Definindo o padrão de comunicação com o socket TCP/IP
client.connect((target_host,target_port))# Criando os parametos de conexão

client.send("*GET / HTTP/1.1\r\nHost:" + target_host + "\r\n\r\n")

response = client.recv(4096)

print response

