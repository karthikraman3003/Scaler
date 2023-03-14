# Example Input
# Input 1:
#
# A = [1, 3, 5, 6]
# B = 5
# Input 2:
#
# A = [1]
# B = 1
#
#
# Example Output
# Output 1:
#
# 2
# Output 2:
#
# 0


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        low = 0
        high = n - 1
        while low <= high:
            middle = (low + high) // 2
            if A[middle] == B:
                return middle
            elif A[middle] < B:
                low = middle + 1
            else:
                high = middle - 1
        return low