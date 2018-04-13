# --*-- coding: utf-8 --*--
import sqlite3

conn = sqlite3.connect('test.db')

sql="""
	insert into saram(id,name,age) values('HONG','GILDONG',33)
"""

c = conn.cursor()
c.execute(sql)

conn.commit()
c.close()