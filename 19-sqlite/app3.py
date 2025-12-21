import sqlite3
class Person:

    @staticmethod
    def create_table_person():
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, age Integer)")
        conn.commit()
        conn.close()

    @staticmethod
    def create_person(first_name, age):
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persons (first_name, age) VALUES (?, ?)", (first_name, age))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_all_persons():
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persons")
        persons = cursor.fetchall()
        conn.close()
        return persons

    @staticmethod
    def delete_person(id):
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM persons WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_person(id, first_name, age):
        conn = sqlite3.connect("db.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE persons SET first_name = ?, age = ? WHERE id = ?", (first_name, age, id))
        conn.commit()
        conn.close()

Person.create_table_person()
Person.create_person("Oren", 38)
persons = Person.get_all_persons()
print(persons)
Person.delete_person(1)
Person.update_person(2, "David", 39)
persons = Person.get_all_persons()
print(persons)