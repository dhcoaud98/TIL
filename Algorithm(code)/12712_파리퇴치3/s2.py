import sys
sys.stdin = open('in1.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_catch = []
    dx_plus = [0, 1, 0, -1]  # 우하좌상
    dy_plus = [1, 0, -1, 0]

    dx_mul = [1, 1, -1, -1] # 우상, 우하, 좌하, 좌상
    dy_mul = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            # + 모양
            my_sum = arr[i][j]
            my_sum_m = arr[i][j]
            for k in range(4):
                for z in range(1, M):
                    # + 모양
                    ni = i + dx_plus[k]*z
                    nj = j + dy_plus[k]*z
                    if 0 <= ni < N and 0 <= nj < N:
                        my_sum += arr[ni][nj]

                    # * 모양
                    ni_m = i + dx_mul[k]*z
                    nj_m = j + dy_mul[k]*z
                    if 0 <= ni_m < N and 0 <= nj_m < N:
                        my_sum_m += arr[ni_m][nj_m]

            max_catch.append(my_sum)
            max_catch.append(my_sum_m)

    print(f'#{tc} {max(max_catch)}')