from  bs4 import BeautifulSoup
import requests , json
from pprint import pprint
url="https://en.wikipedia.org/wiki/Python_(programming_language)"
req=requests.get(url)
#  print (req)
soup=BeautifulSoup(req.text,"html.parser")
# print (soup)
trs=soup.find("table",class_="infobox vevent")
# print(trs)
a=1
for i in trs:
    b=i.get_text()
    # print(b)
    a.append(b)
# print(a)
n=soup.find_all("div",class_="infobox vevent")
dic={}
h=0
for k in n:
    a=k.get_text()
    b=a[h]
    dic[b]=a
    h+=1
    dic[b].update(a)
# print(dic[b])
with open("files.json","w") as open_file:
    json.dump(a,open_file,indent=4)
pprint(a)