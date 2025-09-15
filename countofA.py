name = input("Enter the Names: ")
names = name.split()
print(names)

count=0
for i in names:
    for word in list(i):
        if "a" in word:
            count+=1

print(count)
