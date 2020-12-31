#N,M 입력받기
N,M=map(int,input().split())

arr=[]
min=[]

#이차원 배열 입력받기
for i in range(N):
    arr.append(list(map(int,input().split())))

#이차원 배열을 행별로 정렬하고 가장 작은 수를 min이라는 리스트에 저장
for i in range(N):
    arr[i].sort()
    min.append(arr[i][0])

#min을 정렬하고 가장 큰수를 result에 저장
min.sort()
result=min[N-1]

print(result)