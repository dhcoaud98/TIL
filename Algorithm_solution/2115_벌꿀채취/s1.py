import sys
sys.stdin = open('sample_input.txt')


def DFS(n, cnt, ssum, lst):  # n은 현재 행, cnt는 포함하는지, ssum은 이익, 일꾼의 lst
    global sol

    if cnt > C:
        return

    if n == M:
        if sol < ssum:
            sol = ssum
        return

    DFS(n+1, cnt+lst[n], ssum+lst[n]**2, lst)
    DFS(n+1, cnt, ssum, lst)  # 포함 x

TC = int(input())
for tc in range(1, TC+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    ans = 0
    # 일꾼 1
    for i1 in range(N):
        for j1 in range(1, N-M+1):
            sol = 0
            DFS(0, 0, 0, arr[i1][j1:j1+M])
            t1 = sol
            for i2 in range(i1, N):
                sj = 0
                if i1 == i2:  # 같은 줄이라면?
                    sj = j1+M
                for j2 in range(sj, N-M+1):
                    sol = 0
                    DFS(0, 0, 0, arr[i2][j2:j2+M])
                    ans = max(ans, t1+sol)

    print(f'#{tc} {ans}')