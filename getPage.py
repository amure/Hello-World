#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup
url="https://cn-proxy.com/"
content=urllib.request.urlopen(url)
soup=BeautifulSoup(content)
print(soup)
