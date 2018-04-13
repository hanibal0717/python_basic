# --*-- coding: utf-8 --*--
#python_day03_ex10_sqlite_insert_tuple.py
import sqlite3

conn = sqlite3.connect("test.db")

#튜플로 데이터 매핑할때는 변수 자리에 물음표(?) 사용
sql="""
	insert into saram(id,name,age) values(?,?,?)
"""
tu=('HONG','GILDONG',33)
#튜플 리스트를 이용한 멀티 삽입
tuList=[
	('KIM','GILDONG',33),
	('LEE','GILDONG',65),
	('PARK','GILDONG',85),
	('CHOI','GILDONG',45),
	('KANG','GILDONG',27)
]
c=conn.cursor()
#c.execute(sql, tu)
c.executemany(sql,tuList)

conn.commit() #실행한다. 적용한다.
c.close() #커서를 닫아준다.
conn.close() #접속을 끊는다.