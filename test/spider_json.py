import json

#json数据类型的字符串
str_list = '[1, 2, 3, 4]'
str_dict = '{"city": "北京", "name": "大猫"}'

print(type(str_list))
print(str_list)
print(type(str_dict))
print(str_dict)

#转换成python里面的列表
python_list = json.loads(str_list) # [1, 2, 3, 4]
print(type(python_list))
print(python_list)

python_dict = json.loads(str_dict)
print(type(python_dict))
print(python_dict)