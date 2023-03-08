import socket
import time

#adresa a port serveru
host = "147.229.150.101"
port = 50000

#vytvoreni socketu
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#otevrit kanal
tcp_socket.connect((host, port))

#zaslani dat (odpoved je ukladana do bufferu)
for i in range(5):
    msg = "data" + str(i)
    time.sleep(1)
    tcp_socket.sendall(msg.encode('ascii'))

#prijem
#time.sleep(1)
data = tcp_socket.recv(1024)
print(data)

#uzavreni kanalu
tcp_socket.close()