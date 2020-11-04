#좌표를 입력받기
location=list(input())

#결과값 변수
result=0

#각 케이스에 대한 리스트
c1=[[1,2],[-1,2],[1,-2],[-1,-2]]
c2=[[2,1],[-2,1],[2,-1],[-2,-1]]

#case1
for i in range(4):
    col = int(ord(location[0])) + int(c1[i][0])
    row = int(location[1])+int(c1[i][1])
    if (col<=97 and col>=104 and row>=1 and row <= 8):
        result += 1

#case2
for i in range(4):
    col=int(ord(location[0]))+int(c2[i][0])
    row=int(location[1])+int(c2[i][1])
    if (col<=97 and col>=104 and row>=1 and row <= 8):
        result+=1

#경우의수 출력
print(result)

