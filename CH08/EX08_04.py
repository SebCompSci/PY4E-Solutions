#08.04 Lists
#Open the file 'romeo.txt' and read it line by line.
#For each line split the line into a list of words using the split() method.
#The program shoul build a list of words .
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in pyhton sort() order.

file_name = input("Enter file name: ")
fhand = open(file_name)

unique_words = list()

for line in fhand:
    for word in line.split():
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)
