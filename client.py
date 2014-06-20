from socket import *
import sys
import select

address = ('192.168.1.4', 33333)
client_socket = socket(AF_INET, SOCK_DGRAM)

data = "1|0|0|1"
client_socket.sendto(data, address)

data = "1|0|0|1"
client_socket.sendto(data, address)

data = "0|0|1|0"
client_socket.sendto(data, address)