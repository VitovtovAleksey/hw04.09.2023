import sqlite3

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()


# Задание 2

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        date_birth DATE,
        email TEXT,
        phone TEXT,
        group_name TEXT
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_name TEXT,
    score DECIMAL(3, 2),
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
""")


# Задание 1

cursor.execute("""
CREATE TABLE IF NOT EXISTS VegetablesAndFruits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    color TEXT,
    calories REAL,
    description TEXT
);
""")




conn.commit()
conn.close()


