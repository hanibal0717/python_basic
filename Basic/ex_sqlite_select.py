# --*-- coding: utf-8 --*--
'''
sqlite3 - SELECT 문 작성
'''
#python_day03_ex10_sqlite_select.py

import sqlite3
conn = sqlite3.connect("test.db")

sql="""
	select * from saram
"""

c=conn.cursor()
c.execute(sql)
conn.commit();

# fetchone() - 레코드 한개 가져오기
#print(c.fetchone() )

#여러개의 레코드를 가져오기
#lis = c.fetchmany(3)
#for row in lis:
#	print(row)

#모든 레크드를 가져오기
lis = c.fetchall()
for row in lis:
	print(row)

c.close()
conn.close()