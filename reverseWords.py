# Reverse Words in a string

s = "Deeptech Python Training"
sentence = s.split()
rev_str = ""
for word in sentence:
    rev_str = rev_str + " " + word[::-1]

print(rev_str.strip())  