# dbms_mysql_insert.py
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exampledb2",
    charset="utf8mb4",
    autocommit=False,  # 명시적으로 커밋 제어
)

# 커서 생성 -> 명령어 작성 
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

# ✅ INSERT는 파라미터 바인딩으로 (따옴표/인젝션 문제 예방)
insert_sql = """
    INSERT INTO employees (ID, Name, DeptID, ManagerID)
    VALUES (8, 'Jinny', 2, 101)
    """

cursor.execute(insert_sql)
conn.commit()
print("데이터 삽입 완료")

conn.close()
