import requests
def request_stu():
    # 请求百度
    response = requests.get('http://www.baidu.com')
    print(response)
    # 保存
    with open("百度.html", "wb") as f:
        f.write(response.content)

if __name__ == '__main__':
    request_stu()