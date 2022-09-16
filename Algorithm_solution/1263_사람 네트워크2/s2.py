import sys
sys.stdin = open('input.txt')

def fc(x, nx):

    for j in range(1, N+1):
        if mat[nx][j] == 1 and j not in visited:
            visited.append(j)
            dy[nx][j] = x + 1
            fc(x+1, j)


TC = int(input())
for tc in range(1, 5+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    # print(arr)

    mat = [[0] * (N + 1)]


    for n in range(N):
        next_row = [0] + arr[N*n: N*n+N]
        mat.append(next_row)
    # print(mat)

    for i in range(1, N+1):
        dy = [[0] * (N + 1) for _ in range(N + 1)]
        result = 0
        visited = []
        visited.append(i)
        fc(0, i)
        # print(dy)
        for k in range(1, N + 1):
            result += sum(dy[k])
            # if sum(dy[k]) < answer:
            #     answer = sum(dy[k])
            #     result = k
        print(result)

    answer = float('INF')




    print(f'#{tc} {answer}')