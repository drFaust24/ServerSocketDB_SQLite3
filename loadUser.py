import socket
import sqlite3

## InputSample MESSAGE = "Alice"

con = sqlite3.connect("users.db")
cur = con.cursor()

TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    try:
        data = conn.recv(BUFFER_SIZE)
        print("received data:", data)
        name2 = data[1:-1].decode("utf-8")
        name1 = (name2,)
        res = cur.execute("SELECT * FROM users WHERE name = ?", name1)
        print(str(res.fetchall()))
        con.close()
    except:
        conn.close()