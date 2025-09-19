dict1={"ford":"mustang","chevorlet":"cruze"}
dict2={"suzuki":"fronx"}

dict1.update(dict2)
print(dict1)




n=15
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)




car={"ford":3,"chevorlet":4,"suzuki":5}
sum=0
for i in car.values():
    sum=sum+i
print("sum: ", sum)



car={"ford":3,"chevorlet":4,"suzuki":5}
mul=1
for i in car.values():
    mul=mul*i
print("product: ", mul)
