# Remove duplicate characters of a given string

s = "String and String Function"
words = s.split()
result = []
for word in words:
    if word not in result:
        result.append(word)
output = " ".join(result)
print(output)