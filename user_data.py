import sqlite3

conn = sqlite3.connect('user.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                  username TEXT,
                  password TEXT)''')

cursor.executemany('''INSERT INTO user (username, password) VALUES (?, ?)''', [
    ('user1', '123'),
    ('user2', '456'),
    ('user3', '123456'),
])

cursor.execute("SELECT * FROM user")

rows = cursor.fetchall()

columns = [i[0] for i in cursor.description]

user_list = [dict(zip(columns, row)) for row in rows]

cursor.close()
conn.close()