# 집의 수 입력
n=int(input())

# 집의 위치 입력
houses=list(map(int,input().split()))

total_distance=0
result=[]
for house in houses:
    for i in range(n):
        distance=abs(house-houses[i])
        total_distance+=distance
        result.append([house,total_distance])

result.sort(key=lambda x:x[1])

print(result[0][0])

