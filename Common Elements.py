# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.
#
# NOTE:
#
# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.


A = [1, 2, 2, 1]
B = [2, 3, 1, 2]

dict={}
for i in range(len(A)):
    if A[i] in dict:
        dict[A[i]]+=1
    else:
        dict[A[i]]=1
l=[]
for i in B:
    if i in dict and dict[i]>=1:
        l.append(i)
        dict[i]-=1
print(l)



