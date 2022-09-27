import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 우, 하, 좌, 상 (시계방향)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    my_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:  #ni와 nj는 인덱스
                    if arr[ni][nj] >= arr[i][j]:
                        my_sum += arr[ni][nj] - arr[i][j]
                    else:
                        my_sum += arr[i][j] - arr[ni][nj]


    print(f'#{tc} {my_sum}')
