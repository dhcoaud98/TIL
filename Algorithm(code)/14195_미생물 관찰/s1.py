import sys
sys.stdin = open('sampleinput.txt')


def f(y, x):
    global cnt, A, B
    
    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]

    queue = []
    queue.append([y, x])
    while queue:
        q = queue.pop(0)
        for k in range(4):
            nx = q[1] + dx[k]
            ny = q[0] + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and arr[i][j] == arr[ny][nx]:
                cnt += 1
                visited[ny][nx] = 1
                queue.append([ny, nx])


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)

    A = 0
    B = 0
    max_num = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cnt = 1
            if visited[i][j] == 0:
                visited[i][j] = 1
                f(i, j)
                if arr[i][j] == 'A':
                    A += 1
                elif arr[i][j] == 'B':
                    B += 1

                if max_num <= cnt and (arr[i][j] == 'A' or arr[i][j] == 'B'):
                    max_num = cnt

    print(f'#{tc} {A} {B} {max_num}')
