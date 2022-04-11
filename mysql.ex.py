import pymysql

# Use the pymysql.connect method to connect to the database
db = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123456",database="csdn_crawler",charset='utf-8')
# If you want to operate the database, you also need to get the cursor object on the db
cursor = db.cursor()

# Use cursor.execute to execute sql statements
# cursor.execute("select * from article")
# result = cursor.fetchone()
# print(result)

# Insertion
# sql = "insert into article(id,title,content) value(null,'222','333')"
# cursor.execute(sql)

# title = '444'
# content = '555'
# sql = "insert into article(id,title,content) value(null,%s,%s)"
# cursor.execute(sql,(title,content))

# sql = "select id,title from article where id>2"
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchall()
# print(result)
# result = cursor.fetchmany(2)
# print(result)


# Deletion: delete from table name condition
# sql = "delete from article where id=2"
# cursor.execute(sql)

# # Update data
# sql = "update article set title='钢铁是怎样炼成的' where id=1"
# cursor.execute(sql)

db.commit()
db.close()