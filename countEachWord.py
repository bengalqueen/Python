# Count the occurrences of each word in a given sentence

sentence = "To chnage the overall look of your document. To change the look available in the gallery"
words = sentence.split()
arr = []
for i in words:
    if i not in arr:
        count = 0
        for j in words:
            if i == j:
                count += 1
    print(i, count)