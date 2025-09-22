inp = input("Enter the String: ")
input_list = list(inp)

firstch = input_list[0]
print("firstch :", firstch)

first_found = False

for i in input_list:
    if i == firstch:
        if not first_found:
            print(i)
            first_found = True
        else:
            print("$")
    else:
        print(i)
