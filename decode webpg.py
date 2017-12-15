from bs4 import BeautifulSoup
import requests
url='https://www.nytimes.com'
r=requests.get(url)
r_html=r.text
data=BeautifulSoup(r_html,"html.parser")
title = data.find_all('story-heading')
for i in title:
    if i:
        print(i.text.replace("\n", " ").strip())
    else:
        print(i.contents[0].strip())