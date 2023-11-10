'''Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

input - score - 89
output- B

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

If, elif, else
'''

input_score = int(input("Enter your score\n"))

if 90 <= input_score <= 100:
    print(f"your grade is A")
elif 80 <= input_score <= 89:
    print(f"your grade is B")
elif 70 <= input_score <= 79:
    print(f"your grade is C")
elif 60 <= input_score <= 69:
    print(f"your grade is C")
else:
    print(f"your grade is F")
