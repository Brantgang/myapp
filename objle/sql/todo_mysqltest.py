import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='hello', charset='utf8')
cursor=conn.cursor()
#cursor.execute('insert into man(name,sex) VALUES (%s,%s)',['Richard','1'])
#conn.commit()
#cursor.close()
#cursor=conn.cursor()
cursor.execute('select * from man')
print(cursor.rowcount)
values =cursor.fetchall()
print(values)
cursor.close()
conn.close()