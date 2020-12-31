#N,K 입력받기
N,K=map(int,input().split())

count=0

#1번과 2번의 과정을 반복
while True:
    if N==1:
        break
    if N%K==0:
        N//=K
        count+=1
    else:
        N-=1
        count+=1

print(count)