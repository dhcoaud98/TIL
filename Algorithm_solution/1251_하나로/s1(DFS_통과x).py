import sys
sys.stdin = open('input.txt')


def tax(idx, cnt, N, arr, ssum):
    global min_ssum

    if ssum > min_ssum:
        return

    if cnt == N:
        if ssum < min_ssum:
            min_ssum = ssum
            # print('--', min_ssum)

    
    for i in range(1, N):
        if visited[i] == 0:
            L = ((arr[idx][0]-arr[i][0])**2 + (arr[idx][1]-arr[i][1])**2) * E
            visited[i] = 1
            # print(i)
            # print(ssum + L)
            tax(i, cnt+1, N, arr, ssum+L)
            visited[i] = 0

    return min_ssum


TC = int(input())
for tc in range(1, 2+1):
    N = int(input())
    axis_x = list(map(int, input().split()))
    axis_y = list(map(int, input().split()))
    arr = []
    for a in range(N):
        arr.append([axis_x[a], axis_y[a]])
    print(arr)
    E = float(input())

    visited = [0] * N
    ssum = 0
    min_ssum = float('INF')
    visited[0] = 1  # 시작점은 방문 표시
    print(f'#{tc} {int(tax(0, 1, N, arr, 0))}')
