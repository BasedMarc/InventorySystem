import csv

# Get the input filename from the user
filename = input()

# Create a dictionary to store the word frequencies
word_freq = {}

# Open the input file and read the words
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            # Add the word to the dictionary, or increment its count
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

# Output the word frequencies
for word, freq in word_freq.items():
    print(word, freq)
