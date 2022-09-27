import sys

sys.stdin = open('sample_input.txt')


def f(order):
    global result, num

    if order == N:
        if result > num:
            result = num
        return

    if result <= num:
        return

    for i in range(N):
        if used[i] == 0:  # 방문표시 해주며 더해간다. 
            used[i] = 1
            num += arr[order][i]
            f(order + 1)
            used[i] = 0
            num -= arr[order][i]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    num = 0
    used = [0] * N

    f(0)
    print(f'#{tc} {result}')
