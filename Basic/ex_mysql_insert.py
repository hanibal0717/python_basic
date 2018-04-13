# --*-- coding: utf-8 --*--
import pymysql
conn=pymysql.connect(
	user='root',
	passwd='12345',
	host='localhost',
	db='test',
	charset='utf8'
)

'''
sql="insert into saram values(null,'{0}','{1}',{2})".format('bbb','aaaa',34)
c=conn.cursor()
c.execute(sql)
conn.commit()
'''

def returnRecord():
	id = input("Id >>> ")
	name = input("Name >>> ")
	age = input("Age >>> ")
	return (id, name, age)


#pymysql은 물음표 대신 형식 지정자를 넣는다.
sql="insert into saram values(null,%s,%s,%s)"
#record=('ccc','cccc',30)
record=returnRecord()
c=conn.cursor()
c.execute(sql, record)
conn.commit()

c.close()
conn.close()