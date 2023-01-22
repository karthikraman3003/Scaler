# Count the number of even elemetns in the given range[start,end]
arr=[2,4,5,7,9,8,6,5,4,9]

pf=[]

if arr[0]%2==0:
    pf.append(1)
else:
    pf.append(0)
for i in range(1,len(arr)):
    if arr[i]%2==0:
        val=pf[i-1]+1
    else:
        val=pf[i-1]
    pf.append(val)

q=2
while q:
    start=int(input())
    end=int(input())
    if start==0:
        v=pf[end-1]
    else:
        v=pf[end]-pf[start-1]
    print(v)
    q-=1
