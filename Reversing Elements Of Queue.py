from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        q = deque(A)
        stack = []

        for i in range(B):
            stack.append(q.popleft())

        while stack:
            q.append(stack.pop())

        for i in range(len(q)-B):
            temp=q.popleft()
            q.append(temp)

        s=[]
        for i in q:
            s.append(i)
        return s



A = [ 43, 35, 25, 5, 34, 5, 8, 7 ]
B = 6

sol = Solution()
result = sol.solve(A, B)

print(result) # Output: [4, 5, 1, 2, 3]



