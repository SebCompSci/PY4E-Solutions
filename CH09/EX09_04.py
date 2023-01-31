#09.04 Dictionaries
#Write a program to read through the 'mbox-short.txt' and figure out who has sent the greates amount of mail messages.
#The program looks for 'From' lines and takes the email from the line.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific commiter.

file_name = input("Enter file name: ")
fhand = open(file_name)

mail_dict = dict()
for line in fhand:
    if line.startswith('From '):
        mail = line.split()[1]
        mail_dict[mail] = mail_dict.get(mail, 0) + 1

max_count = 0
for mail, count in mail_dict.items():
    if count > max_count:
        max_count = count
        max_email = mail

print(max_email, max_count)

