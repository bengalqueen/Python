# count Uppercase, Lowercase, Special characters and Numeric values in a given string

s = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper = 0
lower = 0
digit = 0
special = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("UpperCase:", upper)
print("LowerCase:", lower)
print("NumberCase:", digit)
print("SpecialCase:", special)