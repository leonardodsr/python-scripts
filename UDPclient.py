import socket

target_host = input("Host: ")
target_port = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#INET = IPv4, DGRAM = UDP

client.sendto("AAABBBCCC", (target_host,target_port))

data, addr = client.recvfrom(4096)

print data