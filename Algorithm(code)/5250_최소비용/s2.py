def bfs(arrs):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        ci, cj = q.pop(0)
        if ci == N - 1 and cj == N - 1:
            continue

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] - arrs[ci][cj] > 0:
                    if costs[ci][cj] + 1 + arrs[ni][nj] - arrs[ci][cj] < costs[ni][nj]:
                        costs[ni][nj] = costs[ci][cj] + 1 + arrs[ni][nj] - arrs[ci][cj]
                        q.append((ni, nj))
                else:
                    if costs[ci][cj] + 1 < costs[ni][nj]:
                        costs[ni][nj] = costs[ci][cj] + 1
                        q.append((ni, nj))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    costs = [[1000 * 3 * N] * N for _ in range(N)]
    costs[0][0] = 0
    q = [(0, 0)]

    bfs(heights)
    answer = costs[N - 1][N - 1]

    print(f'#{tc} {answer}')