## Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
A = ["abab", "ab", "abcd"]

prefix=A[0]
final_str=''

for i in range(1,len(A)):
    ch=A[i]

    j=0

    while j<min(len(prefix),len(ch)):
        if prefix[j]!=ch[j]:
            break
        j+=1
    prefix=prefix[:j]
print(prefix)








