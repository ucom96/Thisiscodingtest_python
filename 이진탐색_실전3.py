n,m=map(int,input().split())

x=list(map(int,input().split()))

start=0
end=max(x)
result=0

while start<=end:
    mid=(start+end)//2
    total=0
    for i in x:
        if i>mid:
            total+=i-mid
    if total<m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)
