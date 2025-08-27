i=int(input("Enter any number greater than 2 : "))

a=0
b=1

print("Fibonacci series : ")
print(a,",",b,end=",")

for i in range (2,i):
    next=a+b
    print(next,end=",")
    a=b
    b=next