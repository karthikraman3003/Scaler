count=0
def merge(arr, start, middle, end):
    p1=start
    p2=middle+1
    p3=0
    global count
    sorted_arr=[0]*(end-start+1)

    while p1<=middle and p2<=end:
        if arr[p1]<=arr[p2]:
            sorted_arr[p3]=arr[p1]
            p1+=1
        else:
            sorted_arr[p3]=arr[p2]
            p2+=1
            count=count+middle-p1+1
        p3+=1
    while p1<=middle:
        sorted_arr[p3]=arr[p1]
        p1+=1
        p3+=1
    while p2<=end:
        sorted_arr[p3]=arr[p2]
        p2+=1
        p3+=1
    # Returning the sorted data
    arr[start:end + 1] = sorted_arr


def mergesort(arr,start,end):
    if start==end:
        return
    middle=(start+end)//2

    mergesort(arr,start,middle)
    mergesort(arr,middle+1,end)
    merge(arr,start,middle,end)


if __name__ == '__main__':
    A =[ 28, 18, 44, 49, 41, 14 ]
    start=0
    end=len(A)-1
    mergesort(A,start,end)
    print(count)