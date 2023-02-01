#13.02 Using Web Services
#Write a program that prompts for a URL, reads the JSON data using urllib and extract the comment counts, then compute the sum of the numbers.
#The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#       {
#           name: "Matthias"
#           count: 97
#       },
#       {
#           name: "Geomer"
#           count: 97
#       },
#       ...
#   ]
# }

import urllib.request
import json

url = input("Enter URL: ")
fhand = urllib.request.urlopen(url).read()
data = json.loads(fhand)

count_sum = 0
comments = data['comments']
for comment in comments:
    count_sum += int(comment['count'])

print(count_sum)
