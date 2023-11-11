# ✅ Right Triangle Star Pattern
#
# *
# **
# ***
# ****
# *****

rows = 5
for i in range(rows):
    for j in range(i+1):
        print('*', end=' ')
    print("\r")

# Create a Function with a Parameter which can do x^y

# XOR


def xor(x, y):
    a = x ^ y
    return a


i = int(input("enter integer 1"))
j = int(input("enter integer 2"))
print(f" The xor of {i} and {j} is {xor(i,j)}")


# Exponential


def power(m, n):
    result = m ** n
    return result


base = int(input('enter base'))
exponent = int(input('enter exponent'))
print(f"the power of {base} to the {exponent} is {power(base,exponent)}")

# ✅ Create a Lambda expression to triple power 2**3 a number

power_lambda = lambda k: k**3
print(f"the triple power is {power_lambda(2)} ")