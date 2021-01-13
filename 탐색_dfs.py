INF=999999
# 그래프
graph=[[2,3],
       [2,3],
       [0,1],
       [0,1]]
# 방문처리 리스트
visited=[False]*len(graph)
# dfs 함수
def dfs(node,graph,visited):
    visited[node]=True #방문처리
    print(node," ") #출력
    for i in graph[node]: #해당 노드와 연결된 노드들을 차례대로 방문여부 확인
        if visited[i]==False: #방문하지 않았다면
            dfs(i,graph,visited) #재귀함수를 사용하여 똑같은 패턴을 거치도록
        else: #방문을 이미 했다면
            continue #건너뜀

dfs(0,graph,visited)