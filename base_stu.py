#导入库
import random

import requests
import urllib.request
import urllib3
import requests
from requests.adapters import HTTPAdapter

from user_agent import USER_AGENT
from user_proxies import PROXIES_LIST


def hello_spider():
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
   response = requests.get('https://chat1688.xyz/list',headers=headers)
   print(response)
   #保存
   with open("chat1688.html","wb") as f:
      f.write(response.content)


def hello_urlib2_post():
   # urlopen()函数,url是必须要传入的,data如果传入就是POST请求,如果不传就是GETT请求
   response = urllib.request.urlopen("http://www.baidu.com/",
                                     data="s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=尚硅谷".encode("utf-8"))

   # 到服务器返回的数据,读取里面的全部内容
   response_data = response.read()
   # 打印返回的数据
   print(response_data.decode("utf-8"))


def hello_urlib3():
   # 然后你需要一个PoolManager实例来生成请求,
   # 由该实例对象处理与线程池的连接以及线程安全的所有细节，不需要任何人为操作
   http = urllib3.PoolManager()
   # 通过request()方法创建一个请求：
   response = http.request('GET', 'http://www.atguigu.com')
   # request()方法返回一个HTTPResponse对象。
   print(response.status)
   print(response.data.decode("utf-8"))

def hello_requests():
   # response = requests.get("http://www.baidu.com/")
   # 也可以这么写
   # response = requests.request("get", "http://www.baidu.com/")
   # post请求
   response = requests.post("https://chat1688.xyz/auth/login?carid=5.6-p-black")
   # 打印是什么请求
   print(response.request)
   # 打印服务器返回的内容
   print(response.content)

def hello_requests_user_agent_get():

   # kw = {'wd': '尚硅谷'}
   # headers = {
   #    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
   # # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
   # response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
   kw = {'carid': '5.6-p-black'}
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
   # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
   response = requests.get("https://chat1688.xyz/auth/login?", params=kw, headers=headers)
   # 查看响应内容，response.text 返回的是Unicode格式的数据
   print(response.text)
   # 查看响应内容，response.content返回的字节流数据
   print(response.content)
   # 查看完整url地址
   print(response.url)
   # 查看响应头部字符编码
   print(response.encoding)
   # 查看响应码
   print(response.status_code)

def hello_requests_user_agent_post():
   url = "http://httpbin.org/post"
   # url = "http://127.0.0.1:8080"
   # 组装表单数据
   formdata = {"name": "zhangsan", "age": "18"}
   # 请求头
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

   # post请求
   response = requests.post(url, data=formdata, headers=headers)

   print(response.text)
   # 返回url
   print(response.url)
   # 如果是json文件可以直接显示
   print(response.json())

def hello_requests_ajax():
   url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=10"
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
   # 使用get请求得到数据
   response = requests.get(url,headers=headers)
   # 打印返回的数据
   print(response.text)

def hello_requests_proxies():
   # 根据协议类型，选择不同的代理
   # 隧道域名:端口号
   tunnel = "f588.kdltpspro.com:15818"
   # 用户名密码方式
   username = "t11599712367365"
   password = "iesduwvh"
   proxies = {
      "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
      "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
   }
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
   # response = requests.get("http://118.190.202.67:8000/", proxies=proxies)
   # response = requests.get("http://www.baidu.com/", proxies=proxies)
   # response = requests.get("https://chat1688.xyz/endpoint?carid=5.6-p-black", proxies=proxies, headers=headers)
   response = requests.get(" https://chat1688.xyz/list", proxies=proxies, headers=headers)
   print(response.content)
   # 查看完整url地址
   print(response.url)
   # 查看响应头部字符编码
   print(response.encoding)
   print(response.content.decode("utf-8"))

def random_agent_proxy():
   # 模拟浏览器爬取尚硅谷教师的页面
   url = "http://www.atguigu.com/teacher.shtml"

   # 设置模拟不同的浏览器
   user_agent = random.choice(USER_AGENT)

   headers = {"User-Agent": user_agent}

   # 得到不同的代理服务器
   proxies = random.choice(PROXIES_LIST)
   print("当前使用的代理：", proxies)

   print("当前模拟的浏览器是：", headers)

   response = requests.get(url, headers=headers, proxies=proxies)

   print(response.text)

   # with open("尚硅谷教师.html", "wb") as f:
   #    f.write(response.content)

def cookie():
   response = requests.get("http://www.baidu.com/")
   # 7. 返回CookieJar对象:
   cookiejar = response.cookies
   # 8. 将CookieJar转为字典：
   cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
   print(cookiejar)
   print(cookiedict)

def session():
   # 隧道域名:端口号
   tunnel = "f588.kdltpspro.com:15818"
   # 用户名密码方式
   username = "t11599712367365"
   password = "iesduwvh"
   proxies = {
      "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
      "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
   }

   proxies1 = {
      "http": "218.87.205.59:22352",
      "https": "218.87.205.59:22352",
   }
   # 1. 创建session对象，可以保存Cookie值
   ssion = requests.session()
   # 2. 处理 headers
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "zh-TW,zh-CN;q=0.9,zh;q=0.8",
      "Content-Length": "20",
      "Content-Type": "application/json",
   }
   # 3. 需要登录的用户名和密码
   data = {"usertoken": "5df4396d-9f", "action": "default"}
   # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
   # ssion.post("https://chat1688.xyz/auth/login?carid=5.6-p-black", data=data,proxies=proxies,headers=headers)
   # ssion.post("https://chat1688.xyz/carpage", proxies=proxies)
   # https://chat1688.xyz/carpage
   # 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
   # response = ssion.get("https://chat1688.xyz/list",headers=headers)

   req_params = {"page": "1", "size": "50"}
   response = ssion.get("https://chat1688.xyz/carpage", data=req_params, headers=headers)

   # 6. 打印响应内容
   print(response.text)
   with open("偷的gpt.html", "wb") as f:
      f.write(response.content)


if __name__ == '__main__':
    session()
    # hello_requests_proxies
