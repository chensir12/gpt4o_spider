from bs4 import BeautifulSoup
import requests
url = "https://www.douyu.com/directory/all"

html = requests.get(url)
# print(html.text)
#创建 Beautiful Soup 对象
data = html.text
soup = BeautifulSoup(data,"lxml")
#查了标签名为h3的标签
ellipsis_list = soup.find_all('h3')
for ellipsis in ellipsis_list:
   print("ellipsis====================",ellipsis.text.strip())