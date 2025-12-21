config1 = {
    "db_name": "db.db"
}

def get_db_connection():
    conn = sqlite3.connect(config["db_name"])
    return conn

def close_db_connection(conn):
    conn.close()

def get_db_cursor(conn):
    return conn.cursor()

def close_db_cursor(cursor):
    cursor.close()