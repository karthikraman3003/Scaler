A = ["2", "1", "+", "3", "*"]

stack=[]

for i in A:
    if i =='+':
        b=stack.pop()
        a=stack.pop()
        c=a+b
        stack.append(c)
    elif i =='-':
        b=stack.pop()
        a=stack.pop()
        c=a-b
        stack.append(c)
    elif i =='/':
        b=stack.pop()
        a=stack.pop()
        c=a//b
        stack.append(c)
    elif i =='*':
        b=stack.pop()
        a=stack.pop()
        c=a*b
        stack.append(c)
    else:
        stack.append(int(i))
print(stack)









