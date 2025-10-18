import sqlite3
import time

import memcache

db = memcache.Client(['127.0.0.1:11211'])

# db.set('web_page', 'value1', time=3)
# time.sleep(1)
# print(db.get('web_page'))

# db.set('counter',0)
# db.incr('counter',1)
# db.incr('counter',1)
# db.incr('counter',1)
# db.incr('counter',1)
# print(db.get('counter'))

conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
curs.execute(
  'CREATE TABLE persons('
  'employ_id INTEGER PRIMARY KEY AUTOINCREMENT ,'
  'name STRING )')
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()
conn.close()