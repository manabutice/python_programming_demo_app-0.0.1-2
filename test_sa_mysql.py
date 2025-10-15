from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:pass@127.0.0.1:3306/test_mysql_database?charset=utf8mb4",
    echo=True,
    pool_pre_ping=True,
)

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS person_sa(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL
        )
    """))
    conn.execute(text("INSERT INTO person_sa(name) VALUES (:n)"),
                 [{"n":"Alice"},{"n":"Bob"}])
    rows = conn.execute(text("SELECT * FROM person_sa")).all()
    print(rows)
