import mysql.connector

cnn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='staff'
)

cursor = cnn.cursor()

# 读取 SQL 文件内容
with open('staff_staff.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

# 分割 SQL 文件中的语句
sql_statements = sql_script.split(';')

# 执行 SQL 脚本中的每个语句
for statement in sql_statements:
    if statement.strip():
        cursor.execute(statement)

# 执行查询以获取表中的数据
cursor.execute("SELECT * FROM staff")

# 获取查询结果
rows = cursor.fetchall()

# 获取列名
columns = [i[0] for i in cursor.description]

# 转换查询结果为字典列表
salary_list = [dict(zip(columns, row)) for row in rows]

# 关闭游标和数据库连接
cursor.close()
cnn.close()