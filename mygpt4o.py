import json

import requests


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
   # 2. 处理 headers
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
      "Accept":"application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "zh-TW,zh-CN;q=0.9,zh;q=0.8",
      "Content-Length": "20",
      "Content-Type": "application/json",
   }


   # 3.拿到gpt可用的列表，并区分是否plus
   # 查询可用车列表参数
   # req_params = {"page": "1", "size": "50"}
   # ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
   # response = requests.post("https://chat1688.xyz/carpage", json=req_params, proxies=proxies, headers=headers)
   # 打印响应内容
   # print(response.text)
   # rep_str = response.text
   # rep_str = '''{"code":1000,"data":{"list":[{"carID":"5.12-破解","isPlus":1,"status":1},{"carID":"5.18-p-新增","isPlus":1,"status":1},{"carID":"5.18-p-新增-2","isPlus":1,"status":1},{"carID":"5.18-p-新增3","isPlus":1,"status":1},{"carID":"5.18-p-新增4","isPlus":1,"status":1},{"carID":"5.7-p-b","isPlus":1,"status":1},{"carID":"p-5.7-b","isPlus":1,"status":1},{"carID":"5.7浮游","isPlus":1,"status":1},{"carID":"046hugdt","isPlus":1,"status":1},{"carID":"5.3-p","isPlus":1,"status":1},{"carID":"hswczhld","isPlus":1,"status":1},{"carID":"mda2pc5s","isPlus":1,"status":1},{"carID":"t0ydqt4n","isPlus":1,"status":1},{"carID":"v0czu42w","isPlus":1,"status":1},{"carID":"5.2-p","isPlus":1,"status":1},{"carID":"0426有GPTS","isPlus":1,"status":1},{"carID":"gixp7rd4","isPlus":1,"status":1},{"carID":"5e536gar","isPlus":0,"status":1},{"carID":"cneg7tpo","isPlus":0,"status":1},{"carID":"zcsrlkkm","isPlus":0,"status":1},{"carID":"k8nebn1k","isPlus":0,"status":1},{"carID":"pemo1g0l","isPlus":0,"status":1},{"carID":"gj09hahl","isPlus":0,"status":1},{"carID":"6aksfwrj","isPlus":0,"status":1},{"carID":"tx2az9a7","isPlus":0,"status":1},{"carID":"57w70h6u","isPlus":0,"status":1},{"carID":"zoof4gqo","isPlus":0,"status":1},{"carID":"8w2irihl","isPlus":0,"status":1}],"pagination":{"page":1,"size":50,"total":28}},"messages":"success","notice":"\u003ch2 style=\"text-align: center;\"\u003e\u003cspan style=\"color: rgb(36, 41, 46);\"\u003e使用前必看\u003c/span\u003e\u003c/h2\u003e\u003cblockquote\u003e\u003cspan style=\"color: rgb(9, 134, 88);\"\u003e1.\u003c/span\u003e\u003cspan style=\"color: rgb(36, 41, 46);\"\u003e激活码禁止2个设备以上使用，否则会触发风控，直接删除且无售后\u003c/span\u003e\u003c/blockquote\u003e\u003cblockquote\u003e\u003cspan style=\"color: rgb(9, 134, 88);\"\u003e2.\u003c/span\u003e\u003cspan style=\"color: rgb(36, 41, 46);\"\u003e使用方法：选一个4.0的车，点击，输入密码，可以随时换车，次数到了换车即可\u003c/span\u003e\u003c/blockquote\u003e\u003cblockquote\u003e\u003cspan style=\"color: rgb(36, 41, 46);\"\u003e3.有原账号续费需求的，请提前续费，到期账号会自动清除记录\u003c/span\u003e\u003c/blockquote\u003e"}'''
   # loads = json.loads(rep_str)
   # print(loads["code"])



   # 需要登录的用户名和密码
   data = {"usertoken": "5df4396d-9f", "action": "default"}
   # 创建session对象，可以保存Cookie值
   ssion = requests.session()
   # 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
   ssion.post("https://chat1688.xyz/auth/login?carid=5.3-p", data=data, proxies=proxies, headers=headers)
   headers


   # 保存了cookie的会话会有会话列表，解析会话列表，并想办法让流式的输出能得到
   ssion.post("https://chat1688.xyz/backend-api/conversation")


   # with open("mygpt4olist.html", "wb") as f:
   #    f.write(response.content)

if __name__ == '__main__':
    session()