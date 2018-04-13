# --*-- coding: utf-8 --*--

import sqlite3

conn = sqlite3.connect('test.db')
#현재 sqlite를 접속한 폴더안에 db 파일이 생성.
#현재 파일과 같은 폴더에 있다.
#print(conn)

#실행 할 쿼리문을 선언한다.
sql="""
	create table saram(
	no integer primary key,
	id varchar(20),
	name varchar(20),
	age integer
	)
"""

#db를 제어할 커서를 준비한다.
c=conn.cursor()
c.execute(sql)
conn.commit();
c.close()

