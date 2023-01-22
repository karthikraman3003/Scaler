#   Given N array elements and Q queries for each query, calculate sum of all the elements in the given range
# Input arr=[1,2,3,4...n], Q queries value 2, L and R as input values , Find the sum b/w the range(L,R)
arr=[-3,6,2,4,5,2,8,-9,3,1]
pf=[]
pf.append(arr[0])
for i in range(1,len(arr)):
        val=pf[i-1]+arr[i]
        pf.append(val)
q=2
while q:
    l=int(input())
    r=int(input())
    if l==0:
        range_sum=pf[r-1]
    else: range_sum=pf[r]-pf[l-1]
    print(range_sum)
    q-=1
