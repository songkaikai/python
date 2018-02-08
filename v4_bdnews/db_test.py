# coding=utf-8 
# 声明编码方式 默认编码方式ASCII 参考https://www.python.org/dev/peps/pep-0263/ 
import pymysql
 
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="database",charset="utf8")
 
cursor = conn.cursor()
 
sql = "select * from tbk_member"
 
cursor.execute(sql)

print(cursor.rowcount)

 
rows = cursor.fetchall()
 
#print(rows)

for row in rows:
    print('id=%s, username=%s, password=%s, avatar=%s' % row)

cursor.close()
conn.close()

print('id=%s&name=%s' % (2, 's2k'))