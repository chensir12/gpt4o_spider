import requests
import jsonpath
import json

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)"}
response = requests.get(url=url,headers = headers)
#得到json数据是字符串
html = response.text

#loads需要的是字符串
#json.loads接收的是python的类型的
python_dict = json.loads(html)
#python的对象：字典或者列表等
python_list = jsonpath.jsonpath(python_dict,"$..name")

f = open("city.txt","w",encoding="utf-8")
#写入到city.txt文件中,并且是以utf-8编码方式
json.dump(python_list,f,ensure_ascii=False)

print("完毕!")