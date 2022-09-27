# 03.14

## DFS, BFS

<br>

### DFS(Deapth First Search)

:star2: **깊이 우선 탐색**이라고 한다. 시작 점에서 부터 내가 갈 수 있는 경로 가장 깊은 곳 까지 탐색한 후 갈 곳이 없다면 _가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서_다른 방향의 정점으로 탐색을 계속 반복하여 순회하는 방법으로 스택을 사용한다. 재귀 호출을 이용해서 구현한다. 문제를 풀기 위해 정점이 표시된 그래프를 `리스트`혹은 `딕셔너리`를 이용해 표현해야 한다.

```python
def dfs(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            dfs.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited
```



<br>

### BFS(Breadth First Search)

:star2: **너비 우선 탐색**이라고 한다. 이는 담색 시작점의 인접한 정점을 큐의 뒤쪽으로 넣어 탐색하는 방식이다. 한 점에 방문했을 경우 이 점과 인접해 있는 모든 정점들을 큐에 뒤쪽에 삽입하게 되고, 현재 탐색하는 순서는 큐의 앞에부터 순차적으로 이루어지기 때문에 큐를 사용하게 되는 것이다. 

* 두 노드 사이의 최단 경로 
* 임의의 경로를 찾고 싶을 때



```python
def BFS(G,v):  # G는 그래프(딕셔너리 형태임), v는 탐색의 시작지점
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    while queue :  # queue가 비어있다면 종료
        t = queue.pop(0)  # 현재 queue의 첫번째 원소를 t에 넣음.
        # print(t)
        if not visited[t] :  # t에 아직 방문하지 않았다면
            visited[t] = True  # 방문 표시를 남기고
            visit(t)  # visit라는 또 다른 함수에서 할일 하기
        for i in G[t] :  # t와 연결된 모든 정점에서
            if not visited[i]  # 연결된 모든 정점이 방문되지 않았다면
            	queue.append(i)  # 큐에 넣고 while문을 반복한다.
```

