# Count the occurrences of each word in a given sentence

sentence = "To change the overall look of your document. To change the look available in the gallery"
words = sentence.split()
arr = []
for i in words:
    if i not in arr:
        count = 0
        for j in words:
            if i == j:
                count += 1
    print(i, count)

# Optimized Code

sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert sentence to lowercase for consistent counting (optional)
sentence_lower = sentence.lower()

# Split sentence into words
words = sentence_lower.split()

# Dictionary to store word counts
word_count = {}

# Count occurrences
for word in words:
    # Remove punctuation (like the period) if needed
    word = word.strip(".")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(word, count)