

from sqlite3 import Connection

conn = Connection('appdata.sqlite')

with open('createdb.sql', 'r') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
