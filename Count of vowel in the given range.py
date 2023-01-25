# Print the count of number of vowels in the given range of a string
s="tokyolegend"
vowel=['a','e','i','o','u']
pf=[]
c=0
if s[0] in vowel:
    c+=1
    pf.append(c)
else:
    pf.append(c)
for i in range(1,len(s)):
    if s[i] in vowel:
        c+=1
        pf.append(c)
    else:
        pf.append(c)
q=2
while q:
    start=int(input())
    end=int(input())

    if start==0:
        print(pf[end-1])

    else:
        val=pf[end]-pf[start-1]
        print(val)
    q-=1