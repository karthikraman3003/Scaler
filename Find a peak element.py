# Example Input
# Input 1:
#
# A = [1, 2, 3, 4, 5]
# Input 2:
#
# A = [5, 17, 100, 11]
#
#
# Example Output
# Output 1:
#
#  5
# Output 2:
#
#  100
arr =A =  [ 1, 1000000000, 1000000000 ]
n=len(arr)
if arr[n-1]>=arr[n-2]:
    print(arr[n-1])
elif arr[0]>=arr[1]:
    print(arr[0])
else:
    low=1
    high=n-2

    while low<=high:

        middle=(low+high)//2

        if (arr[middle]>arr[middle-1])  and (arr[middle]>arr[middle+1]):
            print(arr[middle])
            high=middle-1
        if arr[middle+1]>arr[middle]:
            low=middle+1
        if arr[middle-1]>arr[middle]:
            high=middle-1
