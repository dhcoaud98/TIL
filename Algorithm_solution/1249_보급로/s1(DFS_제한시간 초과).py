import sys
sys.stdin = open('input.txt')


def fixed(y, x):
    global result, total

    if y == ei and x == ej:  # 마지막에 도달했을 경우
        result = total
        # print(total)

    else:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if total <= result:
                    visited[ny][nx] = 1
                    total += arr[ny][nx]
                    # print(f'{ny, nx}')
                    fixed(ny, nx)
                    visited[ny][nx] = 0
                    total -= arr[ny][nx]

    return result

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [1, 0, -1, 0]  # 우하좌상
    dy = [0, 1, 0, -1]
    result = N*N
    total = 0
    si, sj = 0, 0
    ei, ej = N-1, N-1
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    # print(visited)
    print(f'#{tc} {fixed(si, sj)}')
