"""
DFS와 다른점
1. 가장 밖 while문에서 qeek을 하지 않고 바로 pop을 한다.
(물론 pop 위치도 다르다)
2. 가장 안쪽 if 분기에서 visited 했을 때 break가 없다.
"""

import sys
from pprint import pprint
from collections import defaultdict
from collections import deque

sys.stdin = open('s1.txt')

lst = list(map(int, input().split()))


# 그래프 만들기
graph = defaultdict(list)

for i in range(0, len(lst), 2):
    a = lst[i]
    b = lst[i + 1]
    graph[a].append(b)
    graph[b].append(a)

pprint(graph)


# 큐 만들기
q = deque()
q.append(1)

# 방문표시
visited = [1]

# bfs
while q:
    # 큐에서 pop / DFS와 다른 점은 왼쪽에서 pop함
    tmp = q.popleft()

    """
    visited.append를 아래 if문 안에서가 아니라 여기서 하면 비효율적
    queue를 프린트해보면 queue안에 같은 원소들이 여러번 들어감을 확인할 수 있다.
    queue에 들어갈 때가 아닌 queue에서 나올 때 visited를 확인하기 때문.
    """
    # visited.append(tmp)

    # 해당 값과 연결된 노드에
    for node in graph[tmp]:
        # 방문하지 않았으면
        if node not in visited:
            # 방문표시, q에 append
            # visited.append(node)
            q.append(node)
            print(q)

print(visited)
