import sys
sys.stdin = open('sample_input.txt')

def load(y, x):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = []
    queue.append([y, x])
    visited = [[0]*N for _ in range(N)]
    visited[y][x] = 1

    # 3이 있는 곳 부터 시작하며 진행방향이 길이라면 이동하고, visited에 경로 남겨주기!
    while queue:
        q = queue.pop(0)
        for k in range(4):
            nx = q[1]+dx[k]
            ny = q[0]+dy[k]
            if 0 <= nx < N and 0 <= ny < N and (arr[ny][nx] == 0 or arr[ny][nx] == 2) and visited[ny][nx] == 0:
                queue.append([ny, nx])
                visited[ny][nx] = visited[q[0]][q[1]] + 1

    if visited[end[0]][end[1]] == 0:
        return 0
    else:
        return visited[end[0]][end[1]] - 2

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 3이 있는 곳부터 시작하기!
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                start = [i, j]
            if arr[i][j] == 2:
                end = [i, j]

    print(f'#{tc}', end=' ')
    print(load(start[0], start[1]))

