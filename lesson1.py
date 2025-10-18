from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ---- DB接続（SQLiteのメモリ）----
engine = create_engine("mysql+pymysql:///test_mysql_database2", echo=True, future=True)

# MySQLでやりたい場合（↑の1行と差し替え）
# engine = create_engine(
#     "mysql+pymysql://root:pass@127.0.0.1:3306/test_mysql_database?charset=utf8mb4",
#     echo=True, future=True
# )

Base = declarative_base()

# ---- モデル定義 ----
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(14), nullable=False)

    def __repr__(self):
        return f"Person(id={self.id!r}, name={self.name!r})"

# ---- テーブル作成 ----
Base.metadata.create_all(engine)

# ---- セッション作成 ----
Session = sessionmaker(bind=engine)

session = Session()

p1 = Person(name='Mike')    # 1件追加
session.add(p1)
p2 = Person(name='Nancy')    # 1件追加
session.add(p2)
p3 = Person(name='Jun')    # 1件追加
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

people = session.query(Person).all()
for person in people:
    print(person.id, person.name)
