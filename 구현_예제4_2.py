# 시간을 의미하는 정수 h 입력받기
h=int(input())

#3이 있다면 count 변수에 하나씩 증가
count=0

# 3중 for문을 이용하여 시분초에 3이 있는지 확인할것
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)
