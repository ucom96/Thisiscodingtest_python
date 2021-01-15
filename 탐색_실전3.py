# n,m 입력
n,m=map(int,input().split())

# 얼릴 수 있는 아이스크림의 개수
icecream=0

# 음료수 틀 (그래프)입력
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# dfs함수
def dfs(x,y):
    # 틀의 범위를 벗어날 경우
    if x<0 or y<0 or x>=n or y>=m:
        return False
    # 음료수를 얼릴 수 있는 공간이라면
    if graph[x][y]==0:
        # 방문처리
        graph[x][y]=1
        #상하좌우로 연결된 공간을 찾기
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    #음료수를 얼릴 수 없는 공간이라면
    return False

# 틀의 모든 공간을 하나씩 살피기
for i in range(n):
    for j in range(m):
        # 공간이 음료수를 얼릴 수 있는 공간이라면
        if dfs(i,j):
            icecream+=1

print(icecream)
