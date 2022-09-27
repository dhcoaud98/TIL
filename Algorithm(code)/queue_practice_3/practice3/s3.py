import sys

sys.stdin = open('input.txt')


def bfs():
    # 큐가 비었으면 끝
    if not queue:
        return

    # 뽑아서
    v = queue.pop(0)

    # 방문 체크
    if not visited[v]:
        visited[v] = 1

    # 인접 체크
    for w in G[v]:
        # 방문 안했다면
        if not visited[w]:
            # queue에 넣자
            queue.append(w)

    bfs()


V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V + 1)]  # [[], [], [], [], [], [], [], []]

for i in range(len(temp) // 2):
    G[temp[i * 2]].append(temp[i * 2 + 1])

print(G)  # [[], [2, 3], [4, 5], [7], [6], [6], [7], []]

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
queue = [1]

bfs()

# 방문 확인
for visit, val in enumerate(visited):
    if val == 1:
        print(f'{visit}', end=' ')
