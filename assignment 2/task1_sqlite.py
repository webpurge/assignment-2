import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

students = [
    ("Tendai", 20),
    ("Rudo", 22),
    ("Farai", 21)
]

cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students)
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students in database:")
for row in rows:
    print(row)

cursor.close()
conn.close()
