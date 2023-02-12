A = [0, 0, 0]
B = 0
c=0
for i in range(len(A)):
    for j in range(len(A)+1):
        s=0
        for k in range(i,j):
            s+=A[k]
        if s==B:
            c+=1
print(c)

