from collections import deque
arr=[3,15,6,12,4,2,10,9,13,7,2,5,3]
k=4
dq=deque()
final=[]
for i in range(k):

    while len(dq)>0 and dq[-1]<arr[i]:
        dq.pop()
    dq.append(arr[i])
final.append(dq[0])
for j in range(k,len(arr)):

    if dq[0]==arr[j-k]:
        dq.popleft()

    while len(dq)>0 and dq[-1]<arr[j]:
        dq.pop()
    dq.append(arr[j])
    final.append(dq[0])
print(final)



