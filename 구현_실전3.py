#맵크기 입력
N,M=map(int,input().split()) #int로 설정

#좌표,방향 입력
A,B,d=map(int,input().split()) #int로 설정

#맵상태 입력
state=[]
for i in range(N):
    inputState=list(map(int,input().split()))
    state.append(inputState)

# for i in range(N):
#     for j in range(M):
#         print(state[i][j],end=" ")
#     print()

#방문여부확인
visited = [[0 for i in range(N)] for j in range(M)]
#**현재 좌표는 방문된걸로 처리
visited[A][B]=1

#방향수정함수
def modify():
    global d
    if d==3:
        d=2
    elif d==2:
        d=1
    elif d==1:
        d=0
    elif d==0:
        d=3

#**x좌표,y좌표 이동
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#**시뮬레이션 시작
count=1 #방문한 경로의 수
turn_time=0 #회전수

while True:
    #왼쪽으로 회전
    modify()
    #회전후 좌표바꾸기
    nx=A+dx[d]
    ny=B+dy[d]
    #회전한 곳이 방문하지 않은 곳이라면 왼쪽으로 전진
    if(visited[nx][ny]==0 and state[nx][ny]==0): #**방문할 곳이 육지라는 가정도 필수!
        A = nx
        B = ny
        count+=1 #**방문을 했으니 카운트를 하나 증가시킴
        turn_time=0 #**회전을 한 후 이동했으니 회전수를 다시 초기화시켜야함
    #회전한 곳이 방문한 곳이라면 회전만 수행하고 1단계로 돌아감
    else:
        turn_time+=1
        #continue를 시행하면 안됨
    #네방향 모두 가본 곳이거나 바다로 되어있는 곳이라면 방향을 유지한채로 한칸뒤로 간 후 1단계로 돌아감
    if turn_time==4:
        nx=A-dx[d]
        ny=B-dy[d]
        if(state[nx][ny]==0): #**만약 육지라서 갈 수 있다면
            A=nx
            B=ny
        else: #**만약 바다라서 갈 수 없다면
            break
        turn_time=0

print(count)

