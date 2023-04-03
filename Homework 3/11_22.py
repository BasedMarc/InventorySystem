# Marco Lopez 1537013
# CIS 2348-17255

def main():
    input_words = input()
    words_list = input_words.split()

    word_frequencies = {}

    # Count the frequency of each word in the list
    for word in words_list:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    # Print the words and their frequencies
    for word in words_list:
        print("{} {}".format(word, word_frequencies[word]))


if __name__ == "__main__":
    main()
