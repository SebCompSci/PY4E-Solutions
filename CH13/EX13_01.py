#13.01 Using Web Services
#Write a program that prompts for a URL, reads the XML data from that URL using urllib and then parses and extracts the comment counts from the XML data and computes the sum of the numbers.
#The data consists of a number of names and comment counts in XML as follows:
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
#To make the code a little simpeler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count':
# count_loc = data.findall('.//count')

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
fhand = urllib.request.urlopen(url).read()
data = ET.fromstring(fhand)
count_loc = data.findall('.//count')

num_sum = 0
for count in count_loc:
    num_sum += int(count.text)

print(num_sum)