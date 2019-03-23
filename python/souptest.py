# coding: utf-8
import requests
r = requests.get("http://python123.io/ws/demo.html")
r.headers
r.text
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())
