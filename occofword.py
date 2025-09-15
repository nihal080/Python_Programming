txt = input("Enter the text: ")
words = txt.split()
print(words)

wlist = []
clist = []

for i in words:
    if i in wlist:
        index = words.index(i)
        clist[index] += 1
    else:
        wlist.append(i)
        clist.append(1)

for i in range(len(wlist)):
    print(wlist[i],":",clist[i])
