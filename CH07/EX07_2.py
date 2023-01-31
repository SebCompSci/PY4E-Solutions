#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# 'X-DSPAM-Confidence:    0.8475'
#Count these lines and extract the floating point values from each of the lines and compute the average of those values.
#Do not use the sum() function or a variable named sum in your solution.

file_name = input("Enter file name: ")
fhand = open('file_name')

numb_count = 0
numb_tot = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        numb_loc = line.find('0')
        numb_tot = float(numb_tot) + float(line[numb_loc:])
        numb_count += 1
    else:
        continue

print("Average spam confidence:", numb_tot / numb_count)