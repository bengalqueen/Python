#  Count Vowels in a string

s = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1

print("Total no of vowels:", count)