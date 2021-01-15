from collections import deque

# n,m 입력
n,m=map(int,input().split())

# 맵 정보 입력
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동거리 정보
dx=[-1,1,0,0]
dy=[0,0,-1,1]
start=(0,0)
# bfs 함수
def bfs():
    #큐 생성
    queue=deque()
    queue.append(start)
    # queue가 빌때까지
    while queue:
        x, y = queue.popleft()
        # 상하 좌우로 연결된 노드 찾기
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 노드가 괴물이 없는 공간이라면
            if graph[nx][ny]==1:
                # 이전 노드의 값보다 하나 증가시킴
                graph[nx][ny]+=graph[x][y]
                # 큐에 해당 노드를 삽입
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs())
