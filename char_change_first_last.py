inp = input("Enter the String: ")
input_list = list(inp)

firstch = input_list[0]
lastch = input_list[-1]

str1 = lastch + inp[1:-1] + firstch
print(str1)
