import sys
sys.stdin = open('sample_input.txt')
from collections import deque


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    dx = [1, 0, -1, 0]  # 우하좌상
    dy = [0, 1, 0, -1]

    distance = [[3000*N]*N for _ in range(N)]  # 최소 거리 측정
    # print(distance)
    distance[0][0] = 0

    queue = deque()
    queue.append([0, 0])

    # dijkstra(queue)
    while queue:
        q = queue.popleft()
        for k in range(4):
            nx = q[1] + dx[k]
            ny = q[0] + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] > arr[q[0]][q[1]]:
                    if distance[ny][nx] > 1 + (arr[ny][nx] - arr[q[0]][q[1]]) + distance[q[0]][q[1]]:
                        distance[ny][nx] = 1 + (arr[ny][nx] - arr[q[0]][q[1]]) + distance[q[0]][q[1]]
                        queue.append([ny, nx])
                else:
                    if distance[q[0]][q[1]] + 1 < distance[ny][nx]:
                        distance[ny][nx] = distance[q[0]][q[1]] + 1
                        queue.append([ny, nx])

    print(distance)
    print(f'#{tc} {distance[N-1][N-1]}')
