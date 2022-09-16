import sys
sys.stdin = open('input.txt')


def fc(x, nx):
    """
    :param x: 측정하고자 하는 시작점
    :param nx: 현재 row
    :return:
    """

    for j in range(1, N+1):
        if mat[nx][j] != 0 and j not in visited:
            visited.append(j)
            dy[x][j] = dy[x][nx] + 1
            fc(x, j)


TC = int(input())
# 다익스트라
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    # print(arr)

    mat = [[0] * (N + 1)]
    dy = [[0]*(N+1) for _ in range(N+1)]

    for n in range(N):
        next_row = [0] + arr[N*n: N*n+N]
        mat.append(next_row)
    # print(mat)

    for i in range(1, N+1):
        visited = []
        visited.append(i)
        fc(i, i)

    # print(dy)

    answer = float('INF')
    result = 0

    for k in range(1, N+1):
        # print(sum(dy[k]))
        if sum(dy[k]) < answer:
            answer = sum(dy[k])
            result = k

    print(f'#{tc} {answer}')
