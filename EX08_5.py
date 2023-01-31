#Open the file 'mbox-short.txt' and read it line by line.
#When you find a line that starts with 'From' like the following line:
# 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#You will parse the From line using split() and print out the email address.
#When finished print a count for the total amount of email addresses.
#Make sure not to include lines that start with 'From:'.

file_name = input("Enter file name: ")
fhand = open(file_name)

count = 0
for line in fhand:
    if 'From' in line:
        if 'From:' not in line:
            print(line.split()[1])
            count += 1

print("There were",count, "lines in the file with From as the first word")