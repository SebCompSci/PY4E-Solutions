#10.02 Tuples
#Write a program to read through 'mbox-short.txt' and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#Once you have accumulated the counts for each hour, print out the counts after the hour, sorted by hour.

import os 
os.chdir('C:/Users/vande/Documents/SebCS/GitHub/PY4E-Solutions/CH10')

fhand = open('mbox-short.txt')

hour_dict = dict()
for line in fhand:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        hour_dict[hour] = hour_dict.get(hour, 0) + 1

for hour, count in sorted(hour_dict.items()):
    print(hour, count)