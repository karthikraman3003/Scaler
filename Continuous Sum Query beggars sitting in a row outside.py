# Example Input
# Input 1:-
# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
#
#
# Example Output
# Output 1:-
# 10 55 45 25 25

A = 5
B = [[1, 2, 10],
     [2, 3, 20],
     [2, 5, 25]]
arr=[0]*A
for k in range(0,len(B)):
    i=B[k][0]
    j=B[k][1]
    x=B[k][2]

    arr[i-1]+=x
    if j<A:
        arr[j]=arr[j]-x

pf=[]
pf.append(arr[0])

for i in range(1,A):
    val=pf[i-1]+arr[i]
    pf.append(val)
print(pf)
