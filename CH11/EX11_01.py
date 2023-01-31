#11.01 Regular Expressions
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#We provide 2 files for this assignment.
#One is a sample file where we give you the sum for your testing and the other is the actual data that you need to process for the assignment.
# sample file: 'regex_sum_42.txt' there are 90 values with a sum = 445833.
# acutal data: 'regex_sum_1730540.txt' there are 80 values and the sum ends with 92.
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
    