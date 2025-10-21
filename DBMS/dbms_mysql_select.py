# dbms_mysql.py

import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(

    host = "localhost",
    user = "root",
    password = '1234',
    database = 'exampledb2',
    charset = "utf8mb4",
)

# 커서 생성 -> 명령어 작성
cursor = conn.cursor()

# 명령어 실행
sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)

# sql_departments = "SELECT * FROM departments"
# cursor.execute(sql_departments)
# departments = cursor.fetchall()
# for department in departments:
#     print(department)

print("데이터 조회 완료")
# 연결 해제
conn.close()