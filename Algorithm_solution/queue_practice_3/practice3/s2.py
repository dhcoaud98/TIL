"""
bfs - 인접 행렬 구현
방문체크 시점의 변경
- 이미 방문한 곳을 다시 Queue에 넣는 번거로운 과정을 제거하자!
"""
import sys
from pprint import pprint

sys.stdin = open('input.txt')


def bfs(v):
    queue = [v]
    # 방문표시 먼저 진행 (기존 코드와의 차이점)
    print(v, end=' ')
    visited[v] = 1

    while queue:
        v = queue.pop(0)
        for w in range(1, V + 1):
            if G[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                # print(visited)
                print(w, end=' ')


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
# pprint(temp)

# Graph 초기화
G = [[0] * (V + 1) for _ in range(V + 1)]
# pprint(G)

for i in range(E):
    G[temp[2 * i]][temp[2 * i + 1]] = 1
    G[temp[2 * i + 1]][temp[2 * i]] = 1
# pprint(G)

# 방문 표시 초기화
visited = [0] * (V + 1)
# pprint(visited)

# bfs 탐색 시작
bfs(1)
