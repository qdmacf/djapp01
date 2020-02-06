import pymysql
# 打开数据库连接
# conn = pymysql.connect('rm-m5evc6d1di064l8d4125010.mysql.rds.aliyuncs.com', 'machf', 'Super2020', 'vsmain')
conn = pymysql.connect('rm-m5evc6d1di064l8d4ko.mysql.rds.aliyuncs.com', 'machf', 'Super2020', 'vsmain')
# 使用cursor()方法创建一个游标对象
cursor = conn.cursor()

cursor.execute('SELECT * from vsmain.users')

data =cursor.fetchone()

print("--------------")
print(data)
print("-------this is diff------")


# 关闭数据库连接
conn.close()

