import sqlite3
def create_person(first_name, age):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO persons (first_name, age) VALUES (?, ?)", (first_name, age,))
    print(f"Person {first_name} {age} created")
    conn.commit()
    conn.close()

create_person("david", 38)


