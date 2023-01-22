# An array is said to be equilibrim index if sum of elments before ith index sum[0,i-1]==sum of elements after ith index
# sum[i+1,n-1]

arr=[-3,2,4,-1]
pf=[]
pf.append(arr[0])

for i in range(1,len(arr)):
    val=pf[i-1]+arr[i]
    pf.append(val)
count=0
for i in range(len(pf)):
    left = 0
    if i>0:
        left=pf[i-1]
    right=pf[len(pf)-1]-pf[i]
    if left==right:
        count+=1
print(count)


