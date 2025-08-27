n=int(input("Enter your number"))

def even():
    n%2==0
    return even()

if n%2==0:
    print("Your number is even")
else:
    print("Your number is odd")

