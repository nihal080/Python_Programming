num1= int(input("Enter The first Number: "))
num2= int(input("Enter The Second Number: "))
num3= int(input("Enter The Third Number: "))


if num1 >= num2 and num1 >= num3:
    print("The greatest Number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest Number is", num2)
else:
    print("The greatest Number is", num3)
