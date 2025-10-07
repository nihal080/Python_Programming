def add_suffix(word):
    if word.endswith('ing'):
        return word + 'ly'
    else:
        return word + 'ing'

user_input = input("Enter a word: ")
result = add_suffix(user_input)
print("Result:", result)
