## Unoptimised version T.C  0(N^2), S.C O(N)
import sys
arr=[1,2,3,1,3,4,6,4,6,3]
minimum=sys.maxsize
maximum=0

## Finding minimum and maximum value in an array
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
    elif arr[i]<minimum:
        minimum=arr[i]

### if all the elements in an array is same then min==max,so return 1
if minimum==maximum:
    print(1)

### Follow the format 1. [min....max] , 2. [max...min] in a given array and find the minimum length of subrray contains min and max.
else:
    n=len(arr)
    final=sys.maxsize
    for i in range(len(arr)):
        if arr[i]==minimum:
            for j in range(i+1,n):
                if arr[j]==maximum:
                    final=min(final,j-i+1)
        if arr[i]==maximum:
            for j in range(i+1,n):
                if arr[j]==minimum:
                    final=min(final,j-i+1)
    print(final)
