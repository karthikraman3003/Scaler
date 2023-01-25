# Check if the given list is panagram.A panagram contains all the letters in alphabet(total 26)
arr=["The quick brown fox jumps over the little lazy dog"]
dict=set()
total_alphabet_count=26

for i in arr:
     j=0
     i=i.lower()
     while j<len(i):
         if i[j]!=" ":
            dict.add(i[j])

         j+=1

if total_alphabet_count==len(dict):
    print("True")
else:
    print("False")


