# --*-- coding: utf-8 --*--
import pymysql

conn = pymysql.connect(
	user='root',
	passwd='12345',
	host='localhost',
	db='test',
	charset='utf8'
)

#print(conn)