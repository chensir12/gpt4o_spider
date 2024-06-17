import dmPython

# 配置达梦数据库连接参数
host = '192.168.113.41'  # 替换为你的达梦数据库服务器地址
port = 5236  # 默认端口号
username = 'ODS_WGQ'  # 替换为你的用户名
password = 'easipass1'  # 替换为你的密码
database = 'ODS_WGQ'  # 替换为你的数据库名

# 创建达梦数据库连接
conn = dmPython.connect(
    user=username,
    password=password,
    host=host,
    port=port
)

# 创建游标
cursor = conn.cursor()

# 执行查询
query = 'SELECT * FROM ODS_WGQ.BIGDATA_CENTER_CREDIT_CODE LIMIT 10'  # 替换为你的查询语句
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 打印结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
