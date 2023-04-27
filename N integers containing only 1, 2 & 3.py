from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        l = [1, 2, 3]
        if A == len(l):
            return l
        q1=deque(l)
        q2=deque()
        for i in range(A):
            x=q1.popleft()
            q2.append(x)
            q1.append(int(str(x)+'1'))
            q1.append(int(str(x)+'2'))
            q1.append(int(str(x)+'3'))
        return q2



A=15
obj=Solution()
print(obj.solve(A))

