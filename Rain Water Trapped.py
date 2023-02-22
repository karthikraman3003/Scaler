# Example Input
# Input 1:
#
# A = [0, 1, 0, 2]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
#
# 1
# Output 2:
#
# 0

A = [ 56, 6, 52, 43, 23, 47, 48, 38,
      96, 46, 30, 66, 80, 15, 62, 71, 61, 12, 98, 9, 28, 81,
      70, 59, 95, 34, 9, 60, 70, 81, 71, 67, 58, 20, 22, 3, 95, 85, 20,
      24, 74, 5, 23, 33, 75, 50, 38, 75, 68, 26, 46, 30, 75, 18, 4, 42, 51, 59, 8, 77 ]
n=len(A)
pf=[]
pf.append(A[0])

for i in range(1,n):
    if pf[i-1]<A[i]:
        pf.append(A[i])
    else:
        pf.append(pf[i-1])
# print(pf)

sf=[0]*(n)
val=A[n-1]
sf[n-1]=val

for j in range(n-1,-1,-1):
    if val>A[j]:
        sf[j]=val
    else:
        sf[j]=A[j]
        val=A[j]
# print(sf)
ans=0
for i in range(1,n-1):
    lmax=pf[i-1]
    rmax=sf[i+1]
    level=min(lmax,rmax)
    water=level-A[i]
    if water>0:
        ans+=water
print(ans)
