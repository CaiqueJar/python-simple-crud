import sqlite3

connection = sqlite3.connect('app/database/database.db')


with open("app/database/schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livros (nome, valor, status_atual) VALUES (?, ?, ?)",
            ('Livro #1', 50.00, 'Lido')
            )

connection.commit()
connection.close()