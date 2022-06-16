import sys
sys.stdin = open('input.txt')

def prim(r, N):  # r은 시작, N은 전체 갯수
    MST = [0]*N
    MST[r] = 1
    s = 0  # 가중치의 최소합
    for _ in range(N-1):  # 모든 정점을 돌기 위해
        u = 0
        minV = float('INF')
        for i in range(N):
            if MST[i] == 1:
                for j in range(N):
                    L = ((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)* E
                    if MST[j] == 0 and 0 < L < minV:
                        u = j
                        minV = L

        s += minV
        MST[u] = 1

    return s

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    axis_x = list(map(int, input().split()))
    axis_y = list(map(int, input().split()))
    arr = []
    for a in range(N):
        arr.append([axis_x[a], axis_y[a]])
    E = float(input())

    visited = [0]*N
    print(f'#{tc} {int(round(prim(0, N),0))}')

