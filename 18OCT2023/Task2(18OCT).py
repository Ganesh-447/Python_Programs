# Factorial


number = int(input(" Enter the factorial Number"))

if number < 0:
    print(f"{number} does not have factorial")
else:
    fact =1
    for i in range(1,number + 1):
        fact = fact * i
    print(f"The factorial for {number} is {fact}")