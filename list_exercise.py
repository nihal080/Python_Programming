number=[3,1,4,9,8,2,6]

print("length of the list ")
print(len(number))  

print("The Last Number in List ")
print(number[-1])   

print("List in Reverse")
print(number[::-1]) 

print("Check Number is in List")
if 9 in number:     
    print("The Number 9 is in the List")

print("Insert Number to Last")
number.append(7) 
print(number)
