import sys
sys.stdin = open('input.txt')

def fc(n):
    global answer

    while queue:

        if sum(temp) > answer:  # 가지칙
            break

        p = queue.pop(0)
        for k in range(1, N+1):
            if mat[p][k] == 1 and k not in used:
                temp[k] = temp[p] + 1
                used.append(k)
                queue.append(k)

    if sum(temp) < answer:
        answer = sum(temp)


TC = int(input())
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    # print(arr)

    mat = [[0] * (N + 1)]

    for n in range(N):
        next_row = [0] + arr[N*n: N*n+N]
        mat.append(next_row)
    # print(mat)

    answer = float('INF')

    for i in range(1, N+1):
        queue = []
        used = [i]
        temp = [0] * (N+1)
        for j in range(1, N+1):
            if mat[i][j] == 1:
                queue.append(j)
                used.append(j)
                temp[j] = 1
        fc(i)

    print(f'#{tc} {answer}')