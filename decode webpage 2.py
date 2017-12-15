from bs4 import BeautifulSoup
import requests

url='http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r= requests.get(url)
rhtml=r.text

soup=BeautifulSoup(rhtml,"html.parser")
for i in range(217,306):
   try:
    content=soup.find('section',{'class':'content-section','data-reactid':i})
    for matter in content:
        print(matter.text.replace("\n", " ").strip())

   except AttributeError:
       print ""
   except TypeError:
       print ""
