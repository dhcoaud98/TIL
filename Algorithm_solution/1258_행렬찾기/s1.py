import sys
sys.stdin = open('input.txt')


def dp(y, x):
    global answer, used

    for k in range(1, N):
        if x+k < N and arr[y][x+k] != 0:
            used.append([y, x+k])
        else:
            xlst.append(k)
            while True:
                for n in range(y+1, N):
                    for m in range(x, x+k):
                        if n < N and arr[n][m] != 0:
                            used.append([n, m])
                        else:
                            ylst.append(n-y)
                            return False

            return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    xlst, ylst = [], []
    answer = []
    used = []
    for i in range(N):
        for j in range(N):
            # 0행 or 0열 인 경우
            if arr[i][j] != 0 and [i, j] not in used:
                used.append([i, j])
                dp(i, j)

    for l in range(len(xlst)):
        answer.append([xlst[l]*ylst[l], ylst[l], xlst[l]])

    # print(ylst, xlst)
    print(f'#{tc} {len(xlst)}', end=' ')
    # print(answer)
    answer.sort(key=lambda x: (x[0], x[1]))
    # print(answer)
    for a in answer:
        print(a[1], a[2], end=' ')
    print()

