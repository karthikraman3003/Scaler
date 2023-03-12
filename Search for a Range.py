# Problem Description
# Given a sorted array of integers A (0-indexed) of size N, find the starting and the ending position of a given integer B in array A.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].
#
# Example
# Input
# Input
# 1:
#
# A = [5, 7, 7, 8, 8, 10]
# B = 8
# Input
# 2:
#
# A = [5, 17, 100, 111]
# B = 3
#
# Example
# Output
# Output
# 1:
#
# [3, 4]
# Output
# 2:
#
# [-1, -1]

#  Binary search
arr=[5, 17, 100, 111]
n=len(arr)-1
ans=-1
low=0
high=n
k=3
while low<=high:
    middle=(low+high)//2

    if arr[middle]==k:
        ans=middle
        high=middle-1
    if arr[middle]<k:
        low=middle+1
    if arr[middle]>k:
        high=middle-1
low =0
high=n
ans1=-1
while low<=high:
    middle=(low+high)//2

    if arr[middle]==k:
        ans1=middle
        low=middle+1
    if arr[middle]<k:
        low=middle+1
    if arr[middle]>k:
        high=middle-1
l=[]
l.append(ans)
l.append(ans1)
print(l)