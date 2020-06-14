import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# CREATE TABLE 'PRODUCTS'
cursor.execute('''
CREATE TABLE products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    site TEXT NOT NULL
);
''')

print('Create table sucessfull.')
