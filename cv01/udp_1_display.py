# UDP logger
import struct
import socket

dst_port = 50000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", dst_port))

while True:
    # Receive and unpack the data
    data, address = udp_socket.recvfrom(512)
    
    # Print data
    lg = 'a = {}, p = {}, msg = {}'.format(*address, data)
    print(lg)
