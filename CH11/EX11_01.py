#11.01 Regular Expressions
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+'.
#And then converting the extracted strings to integers and summing them up.

import re

file_name = input("Enter file name: ")
fhand = open(file_name)

numb_sum = 0
for line in fhand:
    if len(re.findall('[0-9]+', line)) > 0:
        numbs = re.findall('[0-9]+', line)
        for numb in numbs:
            numb_sum += int(numb)

print(numb_sum)
    