# 모듈 임포트
import sqlite3, os # os는 운영체제 관련된 내장모듈
from sqlite3 import Error

# 접속 함수
def create_connection(db_file): # db 파일을 하나 입력받는다.
    # ./database 디렉터리 생성
    if not os.path.exists("./database"): # 현재 디렉터리에 database 디렉터리가 없다면
        os.makedirs("./database")

    # 접속
    try:
        conn = sqlite3.connect(db_file) # Connection 객체 리턴
        print(sqlite3.version)
    except Error as e:
        print(e, type(e))
        return None # 접속 실패 시 None 리턴
    return conn

def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()

def test_create_table(db_file):
    # 접속
    conn = create_connection(db_file) # Connection 객체 얻기
    # 커서 획득
    cursor = conn.cursor() # Cursor 객체 얻기
    # sql 작성
    ddl = """CREATE TABLE IF NOT EXISTS
    customer (
        id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))
    """
    # sql 실행
    cursor.execute(ddl)
    # 접속 해제
    conn.close()

# 파라미터를 이용한 insert
def test_insert_data(db_file, name, category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    # 익명 파라미터 바인딩
    sql = """INSERT INTO customer (name, category, region)
    VAlUES(?, ?, ?)"""
    res = conn.execute(sql, (name, category, region))

    # insert, update, delete -> 영향 받은 레코드의 수 .rowcount로 반환
    print("{}개의 레코드가 영향 받음".format(res.rowcount))
    conn.commit()
    conn.close()

# delete
def test_delete_all(db_file):
    conn = create_connection(db_file)
    sql = "DELETE FROM customer"
    res = conn.execute(sql)
    print("{}개의 레코드가 삭제되었습니다.".format(res.rowcount))
    conn.commit()
    conn.close()

def test_insert_bulk_data(db_file):
    test_delete_all(db_file) # 테이블 비우기
    test_insert_data(db_file, "둘리", 1, "부천")
    test_insert_data(db_file, "고길동", 2, "부천")
    test_insert_data(db_file, "김준형", 3, "경기도")
    test_insert_data(db_file, "홍길동", 1, "서울")
    test_insert_data(db_file, "이수민", 2, "부산")

def test_select_data(db_file):
    # conn = create_connection(db_file)
    with create_connection(db_file) as conn: # 추천 -> with문 종료 -> 자동 close()
        # select 쿼리
        sql = "SELECT * FROM customer"
        cursor = conn.execute(sql)

        # print(type(sql))
        # 결과 처리
        print(cursor.fetchone()) # 1개 레코드 불러오기
        print(cursor.fetchmany(2)) # 2개 레코드 불러오기
        print(cursor.fetchall()) # 현재 커서 위치에서 나머지 전체 불러오기
    # conn.close()

def test_search_data(db_file):
    with create_connection(db_file) as conn:
        # 명명된 플레이스 홀더
        # 플레이스 홀더에 :키로 명명
        # 데이터는 dict로 전달
        sql = """SELECT name, category, region FROM customer WHERE region=:region OR category=:category"""

        cursor = conn.execute(sql, {"region":"부천", "category":"2"})

        for customer in cursor.fetchall(): # 전체 레코드 루프
            print(customer)

# 사용자 정의 클래스 임포트
from mysqlite import *
def test_mysqlite_class(db_file):
    # 새 객체 생성
    mydb = Database(db_file)
    sql = """SELECT *FROM customer WHERE region=:region"""
    res = mydb.execute_select(sql, {"region":"서울"})

    for customer in res:
        print(customer)


if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    # test_connection(db_file)
    # test_create_table(db_file)
    # test_insert_data(db_file, '둘리', 2, '부천')
    # test_insert_bulk_data(db_file)
    # test_select_data(db_file)
    # test_search_data(db_file)
    test_mysqlite_class(db_file)