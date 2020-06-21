import requests
from bs4 import BeautifulSoup
from selenium import webdriver
link=input("enter link->")
start_url=link
response = requests.get(start_url)
html = response.text
url_soup = BeautifulSoup(html, 'lxml')
photo_url = url_soup.find("meta", property="og:image")['content']
photo_name = photo_url[-25:-6]
req=requests.get(photo_url)
f=open(photo_name+'.jpg','ab')
f.write(req.content)
f.close()
print("download complete")
    

