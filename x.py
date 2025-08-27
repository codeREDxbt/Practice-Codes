def bookstk():
    print('\n' *5)
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Pop(stk):
    if isEmpty(stk)==True:
        return 'Underflow'
    else:
        a=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
def Push(stk, item):
    stk.append(item)
    top=len(stk)-1
def Display(stk):
    if isEmpty(stk):
        print('Stack is empty.')
    else:
        top=len(stk)-1
        print(stk[top],'<- top')
        for a in range(top-1,-1,-1):
            print(stk[a])
stack=[]
top=None
while True:
    bookstk()
    print('Stack Operations Menu')
    print('1.Push')
    print('2.Pop')
    print('3.Display')
    print('4. Exit')
    ch=int(input('Enter your choice(1-4):'))
    if ch==1:
        bookno=int(input('Enter Book number:'))
        bookname=input('Enter book name:')
        item=[bookno,bookname]
        Push(stack,item)
        input()
    elif ch==2:
        item=Pop(stack)
        if item=='Underflow':
            print('Stack is empty.')
        else:
            print('Last Element added is deleted.')
    elif ch==3:
        Display(stack)
        input()
    elif ch==4:
        break
    else:
        print('Invalid choice!')
        input()

