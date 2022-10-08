# Fast-Sqlite3
Make Your code that clean

# <h1>How To USE?</h1>
```py
from fqlite3 import *
#Make Your fqlite3 Object
fqlite3 = fqlite3()

#Select One Record
select = fqlite3.select_one('users', 'email', 'main.db', id='Hello', name='World') # -> tuple

#cursor.execute('SELECT email FROM users WHERE id == ? AND name == ?;', ('Hello', 'World'))
#cursor.fetchone()

#Select Many Record
select = fqlite3.select_many('users', 'email', 'main.db', id='Hello', name='World') # -> tuple
#
#cursor.execute('SELECT email FROM users WHERE id == ? AND name == ?;', ('Hello', 'World'))
#cursor.fetchall()

#Insert
fqlite3.insert('users', 'main.db', id='Hello', name='World') # -> bool

#cursor.execute('INSERT INTO users VALUES(?, ?);', ('Hello', 'World'))

#Update
fqlite3.insert('users', 'main.db', {id='Hello', name='World'}, email='helloworld@gmail.com') # -> bool

#cursor.execute('UPDATE users SET email = ? WHERE id == ? AND name == ?;', ('helloworld@gmail.com', 'Hello', 'World'))
