# count변수
count=0

# n,m 입력받기
n,m=map(int,input().split())

# 무게리스트 k 입력받기
k=list(map(int,input().split()))

# 이중포문을 이용하여 각 요소들이 다르다면 count를 증가시키기
for i in range(n-1):
    for j in range(i+1,n):
        if k[i]!=k[j]:
            count+=1

print(count)