A=23
temp=str(A)


l=[]
for i in range(len(temp)):
    prod=1
    for j in range(i,len(temp)):
        prod*=int(temp[j])
        l.append(prod)
print(l)
s=set(l)
if len(l)>len(s):
    print(0)
else:
    print(1)

