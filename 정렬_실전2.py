# 수열의 데이터 개수 n 입력받기
n=int(input())

sequence=[]
# 수열의 데이터 입력
for i in range(n):
    sequence.append(int(input()))

# 내림차순으로 정렬 후 공백으로 구분하여 출력
sequence.sort()
sequence.reverse()

for i in sequence:
    print(i,end=" ")