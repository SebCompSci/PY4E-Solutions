#12.03 Network Programming
#Use urllib and BeautifulSoup to read the HTML from the data files below.
#Extract the href= values from the anchor tags, scan for a tag that is in a particular position relative to the first name in that list.
#Follow that link and repeat the process, report the last name you find.
#2 files for this assignment.
#One is a sample file where we give you the name for testing and the other is the actual data you need to process for the assignment.
# sample problem: 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' find the link at position 3, follow that link and repeat this process 4 times. retrieve the last name. 
# Sequence of names: Fikret, Montgomery, Mhairade, Butchi, Anayah.
# actual problem: 'http://py4e-data.dr-chuck.net/known_by_Saoirse.html' find the link at position 18, follow that link and repaat this process 7 times. retrieve the last name.

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