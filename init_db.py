import sqlite3, bcrypt

connection = sqlite3.connect('database.db')

salt = bcrypt.gensalt()
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO staff (full_name, sex, nik) VALUES (?, ?, ?)",
            ('Vincentia', 'F', '1001')
            )
cur.execute("INSERT INTO staff (full_name, sex, nik) VALUES (?, ?, ?)",
            ('Henry', 'M', '1002')
            )

cur.execute("INSERT INTO users (table_id, table_name, email, pwd) VALUES (?, ?)",
            ('1', 'staff', 'vincentiadksitanggang@gmail.com', bcrypt.hashpw('admin', salt))
            )
cur.execute("INSERT INTO users (table_id, table_name, email, pwd) VALUES (?, ?)",
            ('1', 'staff', 'henry@gmail.com', bcrypt.hashpw('admin', salt))
            )

connection.commit()
connection.close()