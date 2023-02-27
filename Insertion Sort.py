A = [4, 2, 1, 1]

for i in range(1,len(A)):
    for j in range(i-1,-1,-1):
        if A[j]>A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
        else:
            break
print(A)
