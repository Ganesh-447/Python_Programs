#Fibonacci Series

number = int(input("enter you number"))
a,b = 0,1

while a < number:
    print(a, end = ' ')
    a,b = b, a+b
    
