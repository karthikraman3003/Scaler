def solve( A, B):
    if B == 0:
        return 0

    for i in range(len(A)):
        if B + A[i] in A:
            return 1

    for j in range(len(A)):
        if B - A[i] in A:
            return 1
    return 0



# Example Input
#
# Input 1:
#
#  A = [5, 10, 3, 2, 50, 80]
#  B = 78
# Input 2:
#
#  A = [-10, 20]
#  B = 30

# Example Output
#
# Output 1:
#
#  1
# Output 2:
#
#  1

A = [5, 10, 3, 2, 50, 80]
B = 78
c=solve(A,B)
print(c)