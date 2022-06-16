import copy
import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    table_mass = [[0]*N for _ in range(N)]  # 크기를 표시해놓은 값
    table_direct = [[0] * N for _ in range(N)]  # 방향을 표시해놓은 값
    time = 1  # 시간 측정
    temp = [[0] * N for _ in range(N)]  # 한 위치에 여러개 군집의 미생물이 모일 대 크기 비교를 위한 값
    arr = []  # 반복을 위한 값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 1. 처음 이동하기
    for i in range(K):
        y, x, start, d = map(int, input().split())

        nx = x + dx[d-1]
        ny = y + dy[d-1]
        if 0 <= nx < N and 0 <= ny < N and (nx == 0 or nx == N-1 or ny == 0 or ny == N-1):
            if d % 2 == 1:  # 방향이 홀수일 경우
                d += 1
            else:  # 방향이 짝수일 경우
                d -= 1
            table_mass[ny][nx] = start//2
            table_direct[ny][nx] = d
        else:
            if table_mass[ny][nx] == 0:  # 기존 table_mass가 비어있을 경우
                table_mass[ny][nx] += start
                temp[ny][nx] = start
                table_direct[ny][nx] = d
            else:  # table_mass가 비어 있지 않은 경우
                if start > temp[ny][nx]:
                    temp[ny][nx] = start
                    table_mass[ny][nx] += start
                    table_direct[ny][nx] = d
                else:  # start < temp[ny][nx]
                    table_mass[ny][nx] += start

    # print(table_mass)
    # print(table_direct)


    # 2. 원하는 시간 만큼 반복하여 움직이기
    temp = [[0] * N for _ in range(N)]
    while time < M:
        temp = [[0] * N for _ in range(N)]  # 한 위치에 여러개 군집의 미생물이 모일 대 크기 비교를 위한 값
        mass = [[0] * N for _ in range(N)]  # 크기를 표시해놓은 값
        direct = [[0] * N for _ in range(N)]  # 방향을 표시해놓은 값
        for i in range(N):
            for j in range(N):
                if table_mass[i][j] != 0:
                    y, x, start, d = i, j, table_mass[i][j], table_direct[i][j]

                    nx = x + dx[d - 1]
                    ny = y + dy[d - 1]
                    if 0 <= nx < N and 0 <= ny < N and (nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1):
                        if d % 2 == 1:  # 방향이 홀수일 경우
                            d += 1
                        else:  # 방향이 짝수일 경우
                            d -= 1
                        mass[ny][nx] = start // 2
                        direct[ny][nx] = d
                    else:
                        if mass[ny][nx] == 0:  # 기존 table_mass가 비어있을 경우
                            mass[ny][nx] += start
                            temp[ny][nx] = start
                            direct[ny][nx] = d
                        else:  # table_mass가 비어 있지 않은 경우
                            if start > temp[ny][nx]:
                                temp[ny][nx] = start
                                mass[ny][nx] += start
                                direct[ny][nx] = d
                            else:  # start < temp[ny][nx]
                                mass[ny][nx] += start

        table_mass = copy.deepcopy(mass)
        table_direct = copy.deepcopy(direct)
        time += 1

    # print(table_mass)
    # print(table_direct)
    result = 0
    for i in range(N):
        for j in range(N):
            if table_mass[i][j] != 0:
                result += table_mass[i][j]

    print(f'#{tc} {result}')

