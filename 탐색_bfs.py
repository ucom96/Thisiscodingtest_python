from collections import deque

# 그래프
graph=[[2,3],
       [2,3],
       [0,1],
       [0,1]]

# 방문처리 리스트
visited=[False]*len(graph)

# bfs함수
def bfs(start,graph,visited):
    queue=deque([start]) #시작 노드를 큐에 삽입
    visited[start]=True #시작 노드를 방문처리

    #큐가 빌때까지 반복
    while queue:
        node=queue.popleft() #큐에서 pop
        print(node,end=" ") #pop한 노드를 출력
        for i in graph[node]: #큐에서 pop한 노드를 기준으로 연결된 모든 노드를 순차적으로 돌음
            if not visited[i]:
                queue.append(i)  # 큐에 삽입
                visited[i] = True  # 방문처리

bfs(0,graph,visited)


