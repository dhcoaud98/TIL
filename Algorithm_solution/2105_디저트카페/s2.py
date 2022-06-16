import sys
sys.stdin = open('sample_input.txt')


def DFS(n, ci, cj, v):
    global si, sj, ans
    if n == 2 and ans >= len(v) * 2:
        return
    if n > 3:  # 종료조건
        return
    if ci == si and cj == sj and n == 3 and ans < len(v):  # 정답 갱신
        ans = len(v)
        return

    for k in range(n, n + 2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v)
            v.pop()

di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    for si in range(0, N - 2):
        for sj in range(1, N - 1):
            DFS(0, si, sj, [])
    print(f'#{test_case} {ans}')