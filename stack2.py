def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
    
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1

def Pop(stk):
    if stk==[]:
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
            return item
        
#main
Stack=[]
top=None
while True:
    print("Stack Operation")
    print("1.Push")
    print("2.Pop")
    print("3.Exit")
    ch=int(input("Enter your item :"))
    if ch==1:
        item=int(input("Enter your number:"))
        Push(Stack,item)
    elif ch==2:
        item=Pop(Stack)
        if item=="Underflow":
            print("Underflow!,the stack is empty")
        else:
            print("popped item is:",item)
    elif ch==3:
        break
    else:
        print("Invalid choice")

    





