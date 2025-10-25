sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

search_word = input("Enter the word to search for: ")
if search_word in words:
    print(f"The word '{search_word}' is present in the sentence.")
else:
    print(f"The word '{search_word}' is not present in the sentence.")
print(f"Number of words in the sentence: {word_count}")
