'''Write a Python program to calculate the area of a circle given its radius using the formula
area=π×r^2 ( Take pie as 3.14)'''

radius = float(input("enter the radius of the circle\n"))
print(f"area of the circle is {3.14* radius ** 2}")

'''Create a program that takes two numbers as input and prints
 whether the first number is greater than, less than, or equal to the second number.'''

number_1 = int(input("enter the number1\n"))
number_2 = int(input("enter the number_2\n"))

if number_1 == number_2:
    print(f"{number_1} and {number_2} are equal")
elif number_1 > number_2:
    print(f"{number_1} is greater")
else:
    print(f"{number_2} is greater")

# Use the ternary operator to find the maximum of three numbers entered by the user.

num_1 = int(input("enter num1"))
num_2 = int(input("enter num2"))
num_3 = int(input("enter num3"))

max = num_1 if (num_1 > num_2 and num_1 > num_3) else num_2 if (num_2 > num_3) else num_3
print(f" The maximum of three number entered by the user are {max}")


# Develop a Python script that calculates the square and cube of a given number.
a = int(input("Enter the number"))
print(f"square and cube of a given number are {a**2} and {a**3}")
