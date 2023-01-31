#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#You should use input to read a string and float() to convert the string to a number.
#Don't worry about error checking or bad user data.

hrs = int(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

pay = str(hrs * rate)
print("Pay:", pay)