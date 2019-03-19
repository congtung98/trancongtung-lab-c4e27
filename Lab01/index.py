import requests
from bs4 import BeautifulSoup
import pyexcel as p

url = 'https://dantri.com.vn/suc-khoe.htm'

response = requests.get(url)

html = response.content.decode('utf-8')

soup = BeautifulSoup(html,'html.parser')

all_div = soup.find_all('div',{'data-boxtype':'timelineposition'})

arr = []
for v in all_div:
    # arr.append([v.div.h2.a.string,v.a.img['src']])
    arr.append({"title":v.div.h2.a.string,"image":v.a.img['src']})
    # print(v.div.h2.a.string)
    # print(v.a.img['src'])
    # print(v.div.div.text)
    # print()
print(arr)
import json
with open('result.json','wt',encoding='utf-8') as f:
    f.write(json.dumps(arr,ensure_ascii=False))