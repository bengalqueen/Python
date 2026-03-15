# Count and display the vowels of a given text

s = "Welcome to python Training"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        print(ch)
        count += 1

print("Total no of vowels:", count)