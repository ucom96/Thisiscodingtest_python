#N,M,K를 공백으로 구분하여 입력받기
N,M,K=map(int,input().split())

#N개의 숫자를 리스트에 저장
data=list(map(int, input().split()))

result=0

#가장 큰 수와 두번째로 큰 수를 찾기
data.sort()
first=data[N-1]
second=data[N-2]

#반복문을 통해 m번 더하기
while True:
    for i in range(K):
        if M==0:
            break
        result+=first
        M-=1

    if M==0:
        break
    result+=second
    M-=1

print(result)

