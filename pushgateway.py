from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from pyhive import hive

# 连接Hive服务器
conn = hive.Connection(host="192.168.113.42", port=10000, username="gcc", password="easipass", auth="LDAP")

# 创建游标
cursor = conn.cursor()

# 执行查询语句
query = "select count(qymc) from ods.ods_bqqy"
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()
number = results[0][0]


# 关闭游标和连接
cursor.close()
conn.close()

# 创建一个新的注册表
registry = CollectorRegistry()

# 创建一个 Gauge 类型的指标
# 'my_custom_metric' 是指标名称，'This is a custom metric' 是指标的描述
metric_1 = Gauge('my_custom_metric', 'This is a custom metric', registry=registry)
metric_2 = Gauge('metric_2', 'Description of metric_2', registry=registry)

# 设置指标的值
metric_1.set(number)  # 你可以将这个值改成你想要推送的实际数值
metric_2.set(number)  # 你可以将这个值改成你想要推送的实际数值

# 推送到 Pushgateway
# 'pushgateway:9091' 是 Pushgateway 的地址和端口，'my_job' 是作业名称
# 'my_instance' 是实例的标签值，用来标识这个指标的来源
push_to_gateway('192.168.113.39:9091', job='my_job', grouping_key={'instance': 'my_instance'}, registry=registry)

print("Metric pushed to Pushgateway successfully!")
