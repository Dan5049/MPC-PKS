# UDP logger
import struct
import socket

dst_port = 50000
file = 'udp_task2.log'

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", dst_port))

while True:
    # Receive and unpack the data
    data, address = udp_socket.recvfrom(512)
    try:
        seq, n1, n2 = struct.unpack("!LLL", data)

    except struct.error:
        # Handle the case where we receive a malformed packet
        print("Unable to unpack packet from {}".format(address))

    else:
        # Save the data
        #print('a = {}, p = {}'.format(address[0],address[1]))
        lg = 'a = {}, p = {}, s = {}, n1 = {}, n2 = {}'.format(*address, seq, n1, n2)
        print(lg)
        fo = open(file, 'a')
        fo.write(lg + '\n')
        fo.close
