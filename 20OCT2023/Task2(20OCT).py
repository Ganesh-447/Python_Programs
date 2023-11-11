number = input("enter input")
result = 0

for i in number:
    digit = int(i)
    result += digit
print(result)


# using Function
def sum_of_integers(n):
    result = 0
    for i in n:
        digit = int(i)
        result += digit
    return result


a = input("enter your input")
print(sum_of_integers(a))

#other method

def sum_of_integers(n):
    sum = 0
    while n > 0:
        mod = n % 10
        sum += mod
        n = n//10
    return sum


a = int(input("enter you number"))
print(f"the sum of the digits of {a} is {sum_of_integers(a)}")