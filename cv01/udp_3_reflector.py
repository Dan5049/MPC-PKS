# UDP reflector
import struct
import socket

dst_port = 50000

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", dst_port))

while True:
    # Receive and unpack the data
    try:
        data, address = udp_socket.recvfrom(512)
        seq, n1, n2 = struct.unpack("!LLL", data)
	
    except struct.error:
        # Handle the case where we receive a malformed packet
        print("Unable to unpack packet from {}".format(address))

    else:
        # Log the message
        lg = 'a = {}, p = {}, s = {}, n1 = {}, n2 = {}'.format(*address, seq, n1, n2)
        print(lg)
        
        # Send back the response
        n2 = seq + n1
        msg = struct.pack("!LLL", seq, n1, n2)
        udp_socket.sendto(msg, address)

