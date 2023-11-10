'''Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.


Input = 2024

Output = Leap year'''

def leap_year_checker(year):
    if ( year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
        return 'Leap Year'
    else:
        return 'not a Leap year'

y = int(input("enter the year"))
print(f"The given year {y} is {leap_year_checker(y)}")



