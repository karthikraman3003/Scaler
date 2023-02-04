# Problem Description
# Given an integer array A containing N distinct integers.
#
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
#
# NOTE:
#
# Pair (a, b) and (b, a) is considered to be the same and should be counted once.
#
# Input 1:
#
#  A = [5, 4, 10, 15, 7, 6]
#  B = 5
# Input 2:
#
#  A = [3, 6, 8, 10, 15, 50]
#  B = 5
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  2

A = [3, 6, 8, 10, 15, 50]
B = 5

dict={}
c=0

for i in range(len(A)):
    val=A[i]^B
    if val in dict:
        c+=1
    else:
        dict[A[i]]=1
print(c)