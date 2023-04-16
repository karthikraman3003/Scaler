A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]
stack=[]
for i in range(len(C)):
    if C[i]==0:
        stack.pop()
    else:
        stack.append(C[i])
print(stack[len(stack)-1])
