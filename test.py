import socket
import json
while(1):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 55000
 #   MESSAGE = {"name": "Betty", "lvl": "2", "Score": "5"}
    MESSAGE = "Alice"
    data = json.dumps(MESSAGE)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.sendall(bytes(data,encoding="utf-8"))
#    s.send(bytes(MESSAGE, encoding="utf-8"))
    s.close()
