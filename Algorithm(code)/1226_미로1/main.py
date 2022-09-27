import sys
sys.stdin=open('input.txt')


def load(m):
    # 현재 나의 위치를 기반으로 상하좌우의 값이 0 혹은 3이라면 my_load에 추가한다.
    # 그 후 my_load의 0번째 값을 꺼내면서 visited에 넣는다. 만약  my_load가 비게 되면 종료한다.
    # 종료 후에는 visited에 3의 좌표값이 있으면 1, 없으면 0을 출력하도록 한다.
    dx = [0, 0, 1, -1]  # 상하좌우
    dy = [-1, 1, 0, 0]
    visited = [m]
    my_load = [m]
    while my_load:
        v = my_load.pop(0)
        for k in range(4):
            nx = v[1] + dx[k]
            ny = v[0] + dy[k]
            if matrix[ny][nx] == 0 or matrix[ny][nx] == 3:
                if [ny, nx] not in visited:
                    my_load.append([ny, nx])
                    visited.append([ny, nx])

    if [end[0], end[1]] in visited:
        return 1
    else:
        return 0


for t in range(10):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]

    # 1. 2와 3의 위치 찾기
    start = []
    end = []
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start.append(i)
                start.append(j)
            if matrix[i][j] == 3:
                end.append(i)
                end.append(j)

    print(f'#{tc} {load(start)}')

