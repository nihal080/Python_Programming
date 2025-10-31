txt = input("Enter The Text: ")
vow = ["a", "e", "i", "o", "u"]
lst = []

for i in txt:
    if i.lower() in vow:
        lst.append(i)

print(lst)
