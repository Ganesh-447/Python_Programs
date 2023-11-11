# Task 1
# Count vowels and consonants in a String
# aeiou
# input = pramod
# vol = 2

a = input('enter you string \n')
count = 0
cons = 0

for i in a:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
            i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        count += 1
    else:
        cons += 1

print(f"The vowels in {a} are {count}")
print(f"The consonants in {a} are {cons}")
