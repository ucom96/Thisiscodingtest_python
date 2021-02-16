def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1

    return None

n=int(input())
array=list(map(int,input().split()))
# 이진탐색을 하기 위해 미리 정렬
array.sort()
m=int(input())
x=list(map(int,input().split()))

# x의 요소 하나씩 target으로 잡아 확인
for i in x:
    result=binary_search(array,i,0,n-1)
    if result!=None:
        print("yes",end=' ')
    else:
        print("no",end=' ')