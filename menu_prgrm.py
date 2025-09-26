while True:
    print("MENU Options")
    print("1. Occurrence of a Word")
    print("2. Character frequency")
    print("3. Display the factors of a given number")
    print("4. Exit")
    inp = int(input("Enter The Choice: "))

    if inp == 1:
        print("OCCURRENCE OF A WORD")
        txt = input("Enter the text: ")
        words = txt.split()
        print(words)

        wlist = []
        clist = []

        for i in words:
            if i in wlist:
                index = wlist.index(i)
                clist[index] += 1
            else:
                wlist.append(i)
                clist.append(1)

        for i in range(len(wlist)):
            print(wlist[i], ":", clist[i])

    elif inp == 2:
        print("CHARACTER FREQUENCY")
        inp = input("Enter the Word: ")
        if not inp.strip():
            print("No input provided.")
        else:
            words = inp.split()
            for wrd in words:
                print(f"\nWord: {wrd}")
                counts = {}
                for ch in wrd:
                    ch_lower = ch.lower()
                    counts[ch_lower] = counts.get(ch_lower, 0) + 1
                for ch, count in counts.items():
                    print(f"{ch} - {count}")

    elif inp == 3:
        print("FACTORS OF A GIVEN NUMBER")
        number = int(input("Enter a number: "))
        print(f"Factors of {number} are:")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)

    elif inp == 4:
        print("EXITING....")
        break

    else:
        print("Invalid choice, please select 1, 2, 3, or 4")
