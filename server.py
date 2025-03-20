#print(1)

import socket

#HOST = socket.gethostname()

HOST = ('127.0.0.1', 7771)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST)
sock.listen()

print("---START---")
conn, addr = sock.accept()

print(conn)
print(addr)

print("---end---")

#print(HOST)