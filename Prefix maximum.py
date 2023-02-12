# Input 1:
#
# A = [9, 7, 6, 18, 2]
# Input 2:
#
# A = [16, 8, 24, 9, 25, 17]
#
#
# Example Output
# Output 1:
#
# [9, 9, 9, 18, 18]
# Output 2:
#
# [16, 16, 24, 24, 25, 25]

A = [16, 8, 24, 9, 25, 17]

pf=[]
pf.append(A[0])

for i in range(1,len(A)):
    if pf[i-1]>A[i]:
        pf.append(pf[i-1])
    else:
        pf.append(A[i])

print(pf)