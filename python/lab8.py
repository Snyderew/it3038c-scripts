from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://loudwire.com').content
soup = BeautifulSoup(r, "lxml")
print(type(soup))
print(soup.prettify()[:100])
for title in soup.find_all('a', attrs={'class':re.compile("^title")}):
    print(title.text.strip())
    
