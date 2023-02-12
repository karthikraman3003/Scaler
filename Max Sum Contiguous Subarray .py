# Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.

import sys
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sum=0
ans=-sys.maxsize

for i in range(len(A)):
    sum+=A[i]
    ans=max(ans,sum)
    if sum<0:
        sum=0
print(ans)