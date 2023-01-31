#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None

while True:
    number = input("Enter number: ")
    if number.lower() == 'done':
        break
    
    try:
        number = int(number)
    except:
        print("Invalid input")
        continue

    if largest is None or largest < number:
        largest = number
    if smallest is None or smallest > number:
       smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)

