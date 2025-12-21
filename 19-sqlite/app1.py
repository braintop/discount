import sqlite3

conn = sqlite3.connect("db1.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, age Integer)")

cursor.execute("INSERT INTO persons (first_name, age) VALUES (?, ?)", ("Oren", 38))

conn.commit() #save the changes
conn.close() #close the connection