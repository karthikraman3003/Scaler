# Example Input
# Input 1:
#
# A = [4, 7, 9 ]
# B = [2, 11, 19 ]
# Input 2:
#
# A = [1]
# B = [2]
#
#
# Example Output
# Output 1:
#
# [2, 4, 7, 9, 11, 19]
# Output 2:
#
# [1, 2]

A = [1]
B = [2]
len_a=len(A)
len_b=len(B)
c=[]
p1=0
p2=0

while (p1<len_a) and (p2<len_b):
    if A[p1]<B[p2]:
        c.append(A[p1])
        p1+=1
    else:
        c.append(B[p2])
        p2+=1

while p1<len_a:
    c.append(A[p1])
    p1+=1
while p2<len_b:
    c.append(B[p2])
    p2+=1
print(c)



