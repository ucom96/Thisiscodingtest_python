n=map(int,input())
x=list(map(int,input().split()))

count=0
result=0

x.sort()

for i in x:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)