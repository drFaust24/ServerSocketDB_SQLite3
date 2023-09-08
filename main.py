import socket
import sqlite3
import json

## InputSample MESSAGE = {"name": "Betty", "lvl": "2", "AnonScore": "5"}

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
        obj = json.loads(data)
        print(obj)
        cur.executemany("INSERT INTO users (name, lvl, Score) VALUES (:name, :lvl, :Score)", [obj])
        con.commit()
        print("Stored")
        res = cur.execute("SELECT * FROM users")
        print("\n" + str(res.fetchall()))
        conn.close()
    except:
        conn.close()