import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    problem TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()

print("Database Created")