# --*-- coding: utf-8 --*--
import sqlite3

conn = sqlite3.connect("test.db")

sql="""
	delete from saram where no=%s and name=%s
"""
# 조건값으로 변수를 사용
no = 3

c = conn.cursor()
c.execute(sql %(no, "HONG"))
conn.commit()
c.close()