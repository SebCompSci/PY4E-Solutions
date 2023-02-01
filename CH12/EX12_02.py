#12.02 Network programming
#Write a program the uses urllib and BeautifulSoup to read the HTML from the data files below, and parse the data.
#Extract the numbers and compute the sum of the numbers in the file.
#Data format:
# '<tr><td>Modu</td><td><span class="comments">90</span></td></tr>'
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url: ")
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

numb_sum = 0
for line in soup('span'):
    numb_sum += int((line.text))

print(numb_sum)