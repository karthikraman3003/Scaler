# Example Input
# Input 1:
#
# A = [12, 5, 6, 7]
# Input 2:
#
# A = [15, 9, 7, 11, 10]
#
#
# Example Output
# Output 1:
#
# [12, 7, 7, 7]
# Output 2:
#
# [15, 11, 11, 11, 10]

A = [15, 9, 7, 11, 10]

n=len(A)
pf=[0]*n
val=A[n-1]
pf[n-1]=val

for i in range(n-1,-1,-1):
    if val>A[i]:
        pf[i]=val
    else:
        pf[i]=A[i]
        val=A[i]
print(pf)