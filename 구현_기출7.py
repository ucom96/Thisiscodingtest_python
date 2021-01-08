# 정수형 데이터 입력받기
score=input()

# 정수형 데이터 길이 변수
length=len(score)

summary=0
# 앞의 데이터들의 합
for i in range(length//2):
    summary+=int(score[i])

# 뒤의 데이터들의 합을 빼줌
for i in range(length//2,length):
    summary-=int(score[i])

if summary==0:
    print("LUCKY")
else:
    print("READY")




