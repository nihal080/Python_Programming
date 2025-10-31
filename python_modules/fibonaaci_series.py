def fibonnaci(num):    
    n1=0
    n2=1
    count=0
    if num <= 0:
        print("Enter a +ve number")
    elif num == 1:
       print("Fibonacci sequence :",n1)
    else:
       print("Fibonacci sequence:")
       while count < num:
           print(n1)
           n3=n1+n2
           n1=n2
           n2=n3
           count=count+1

#num_term=int(input("Enter The Number : "))
#fibonnaci(num_term)
