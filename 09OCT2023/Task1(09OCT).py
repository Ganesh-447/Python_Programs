a=[]
for i in range(5):
    x=int(input("enter your numbers for 5 times\n"))
    a.append(x)
non_duplicate=set(a)
print("The non duplicates numbers are",non_duplicate)