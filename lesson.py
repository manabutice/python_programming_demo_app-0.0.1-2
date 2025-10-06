import os, sqlite3

# db_path = os.path.abspath("test_sqlite.db")  # 絶対パスに固定
conn = sqlite3.connect(':memory:')
# print("DB path:", db_path)

curs = conn.cursor()

# テーブルが無ければ作る（初回のみ）
curs.execute("""
CREATE TABLE IF NOT EXISTS persons(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
)
""")
conn.commit()

# ここでは INSERT しない
curs.execute("DELETE FROM persons")
curs.execute('INSERT INTO persons(name) values("Nancy")')
curs.execute('INSERT INTO persons(name) values("Jun")')
conn.commit()

curs.execute('UPDATE persons set name = "Michel" WHERE "Mike"')

curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()
# 中身を表示
curs.execute("SELECT * FROM persons")
# for row in curs.fetchall():
print(curs.fetchall())

curs.close()
conn.close()
