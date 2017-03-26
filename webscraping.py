# requests - get the website
# beautifulsoup (bs4) - analyze the website

import requests
from bs4 import BeautifulSoup

# loading webpage
r = requests.get('http://pythonhow.com/example.html')

#grabbing the content
c = r.content
# print(c)

# beaufitul soup is parsing the code of the website
soup=BeautifulSoup(c,"html.parser")

# pretify makes the website code prettier
# print(soup.prettify())

# listing elements of website
all=soup.find_all('div',{'class':'cities'})
only_one=soup.find('div',{'class':'cities'})
# print(all)
# print(only_one)

# listing specific element using list indexing
specific = soup.find_all('div',{'class':'cities'})[0]
# or all[0]

# goind deeper, finding h2 tag within div
print(all[0].find_all('h2')[0].text)

# finding all cities from the website

for item in all:
    print(item.find_all('h2')[0])
