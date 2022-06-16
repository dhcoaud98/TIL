import sys
from collections import deque
sys.stdin = open('input.txt')


def BFS(queue):

    while queue:
        q = queue.popleft()
        for k in range(4):
            nx = q[1] + dx[k]
            ny = q[0] + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if distance[ny][nx] > distance[q[0]][q[1]] + arr[ny][nx]:
                    distance[ny][nx] = distance[q[0]][q[1]] + arr[ny][nx]
                    queue.append([ny, nx])


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [1, 0, -1, 0]  # 우하좌상
    dy = [0, 1, 0, -1]

    INF = float('inf')  # 무한대로 가정!
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0

    queue = deque()
    queue.append([0, 0])

    BFS(queue)
    print(f'#{tc} {distance[N-1][N-1]}')