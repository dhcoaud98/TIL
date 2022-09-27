import sys
sys.stdin = open('sample_input.txt')


def DFS(n):
    global total, result

    if n == 0:
        # print(total)
        if result >= total:
            result = total
        return

    stack = []
    stack.append(n)
    p = stack.pop()
    for k in range(M):
        if temp[k][p] != 0:
            if total <= result:
                total += temp[k][p]
                DFS(k)
                total -= temp[k][p]


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    temp = [[0]*M for _ in range(M)]

    for m in range(M):
        i, j, v = map(int, input().split())
        temp[i][j] = v
    # print(temp)
    result = 10000000

    # N에서 0으로 가는 모든 경로를 구하기
    total = 0
    DFS(N)
    print(f'#{tc} {result}')
