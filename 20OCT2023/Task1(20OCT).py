'''Palindrome Checker:
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121

Example - pramod
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam

Compare String with the Revserse of the string
'''

#using slicing.
a_string = input("enter your string")
b_string = a_string[::-1]
if a_string == b_string:
    print(f"{a_string} is a palindrome")
else:
    print(f"{a_string} is not a palindrome")

