#03.01 Conditional Execution
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate fpr the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#You should use input to read a string and float() to convert the string into a number.
#Do not worry about error checking the user input.

hrs = int(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

if hrs > 40:
    pay = (40 * rate) + ((hrs - 40) * ( rate * 1.5))
else:
    pay = hrs * rate

print(pay)