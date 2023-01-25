# Optmised Version T.C 0(N),S.C O(N)
import sys
arr=[1,6,4,6,5,1,5,2,6,4,4,2,1,5]
minimum=sys.maxsize
maximum=0
## Find the minimum and maximum value in given array
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
    if arr[i]<minimum:
        minimum=arr[i]


n=len(arr)-1

## Assign the maximum value of final as length of array bcz we need minimum final
final=n

new_min_start=-1
new_max_start=-1

##  Iterate the array from -1 to 0
### Check the max_new_start !=-1 or new_min_start!=-1 bcz this is the corner cases
##  Update the ans when values is minind then sub it with (maxind-minind+1), similarly for maxind we have to sub (minind-maxind+1)
for i in range(n,-1,-1):
    if arr[i] == minimum:
        new_min_start = i

        if new_max_start!=-1:
            final = min(final, new_max_start-new_min_start+1)
    elif arr[i] == maximum:
        new_max_start = i
        if new_min_start!=-1:
            final = min(final, new_min_start-new_max_start+1)

print(final)
