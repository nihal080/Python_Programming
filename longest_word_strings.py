words = input("Enter The Words: ").split()
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)

print("Length of the longest word:",word ," : ", longest)
