#12.03 Network Programming
#Use urllib and BeautifulSoup to read the HTML from the data files below.
#Extract the href= values from the anchor tags, scan for a tag that is in a particular position relative to the first name in that list.
#Follow that link and repeat the process, report the last name you find.

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url: ")
pos = int(input("Enter position: ")) - 1
rpt = int(input("Enter repetitions: ")) + 1

while rpt > 0:
    rpt -= 1
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    link = soup('a')
    url = link[pos].get('href')

name = (soup.title.string).split()[2]
print(name)