#to cheack wether stack empty or not
def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
#using push to input item in stack
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
#using pop to out the last input item
def Pop(stk):
    if isempty(stk):
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
    print("STACK OPERATION")
    print("1.Push")
    print("2.Pop")
    print("3.Exit")
    ch=int(input("Enter choice(1-3):"))
    if ch==1:
        item=int(input("Enter the item:"))
        Push(Stack,item)
    elif ch==2:
        item=Pop(Stack)
        if item=="underflow":
            print("Underflow! stack is empty")
        else:
            print("poped item is:",item)
    elif ch==3:
        break
    else:
        print("Invalid choice")