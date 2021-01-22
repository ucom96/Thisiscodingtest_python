# N,K 공백으로 입력
n,k=map(int,input().split())

# A 원소 입력
a=list(map(int,input().split()))

# B 원소 입력
b=list(map(int,input().split()))

# a를 오름차순으로 정렬
a=sorted(a)

# b를 내림차순으로 정렬
b=sorted(b,reverse=True)

# k번동안 a와 b의 요소를 바꿔치기
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# a의 요소합의 최댓값을 구하기
print(sum(a))

