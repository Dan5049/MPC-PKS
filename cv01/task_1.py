import socket
import struct
import time

file = "udp.log"

#adresa a port prijemce (zada vyucujici)
dst_host = "147.229.150.101"
dst_port = 50000
src_port = 60000

#vytvoreni socketu
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", src_port))
udp_socket.settimeout(5)

for i in range(5):
    seq = i
    n1 = 75
    n2 = 10

    #zaslani zpravy
    msg = struct.pack("!LLL", seq, n1, n2)
    n = udp_socket.sendto(msg, (dst_host, dst_port))
    print("Odeslano {} byte\n".format(n))

    try:
        msg, address = udp_socket.recvfrom(512)
        Rseq, Rn1, Rn2 = struct.unpack("!LLL", msg)
    except TimeoutError:
        print("No response from server")
    except struct.error:
        print("Unable to unpack packet from {}".format(address))
    else:
        lg = "a={}, p={}, s={}, n1={}, n2={}".format(*address, Rseq, Rn1, Rn2)
        print(lg)
        fo = open(file, "a")    #soubor otevřít v řežimu “append”
        fo.write(lg + "\n")     #přidat znak nového řádku
        fo.close
        time.sleep(0.5)

#uzavreni socketu
udp_socket.close()
