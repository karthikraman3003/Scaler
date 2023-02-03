# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
#
# If the answer does not exist return an array with a single element "-1".
#
# First sub-array means the sub-array for which starting index in minimum.

# Input 1:
#
#  A = [1, 2, 3, 4, 5]
#  B = 5
# Input 2:
#
#  A = [5, 10, 20, 100, 105]
#  B = 110
#
#
# Example Output
# Output 1:
#
#  [2, 3]
# Output 2:
#
#  -1

A = [ 1, 1000000000 ]
B = 1000000000

left=0
right=0

end=len(A)
curr_sum=0
for i in range(len(A)):

    curr_sum += A[i]
    right += 1
    while curr_sum>B and left<right:
            curr_sum-=A[left]
            left+=1
    if curr_sum==B:
        print(A[left:right])






