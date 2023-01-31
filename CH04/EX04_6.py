#Write a program to prompt the user for hours and rate per hour using input to compute the gross pay.
#Pay should be the normal rate for hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
#The function should return a value.
#You should use input to read a string and float to convert the string into a number.
#Do not name your variable sum or use the sum() function.

hrs = int(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

def computepay(h, r):
    if h > 40:
        return (40 * r) + ((h - 40) * (r * 1.5))
    else:
        return h * r

print("Pay", computepay(hrs, rate))

