# Count and display the vowels of a given text

s = "Welcome to python Training"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        print(ch)
        count += 1

print("Total no of vowels:", count)

# Optimized code

# Given text
text = "Welcome to python Training"

# Convert text to lowercase for uniformity
text_lower = text.lower()

# Set of vowels
vowels = "aeiou"

# Dictionary to store vowel counts
vowel_count = {}

# Count vowels
for char in text_lower:
    if char in vowels:
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1

# Display vowel counts
print("Vowel counts in the text:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")