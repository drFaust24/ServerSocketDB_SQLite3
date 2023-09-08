import sqlite3

con = sqlite3.connect("users.db")

con.cursor().execute("CREATE TABLE users(name, lvl, Score)")

print("Base created")
