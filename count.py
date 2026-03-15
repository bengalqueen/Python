# count all letters, digits and special symbols from the given string

s = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0
for ch in s:
    ascii_val = ord(ch)
    if ((ascii_val >= 65 and ascii_val <= 90) or (ascii_val >= 97 and ascii_val <= 122)):
        letters += 1
    elif (ascii_val >= 48 and ascii_val <= 57):
        digits += 1
    else:
        symbols += 1

print("Chars:", letters)
print("Digits:", digits)
print("Symbols:", symbols)