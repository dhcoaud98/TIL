import sys
from pprint import pprint
sys.stdin = open('input.txt')

# 1. 기본 입력사항
n, m = map(int, input().split(' '))
# print(n, m)

result = 0
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

# input 그리기
# pprint(matrix)

virus = []
load = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus.append((i, j))
        if matrix[i][j] == 0:
            load.append((i, j))

pprint(f'virus: {virus}')
pprint(f'load: {load}')


#################

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 바이러스 감염 (bfs)
def spread_virus(temp_map):
    check = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    temp_virus = virus[:]
    while temp_virus:
        x, y = temp_virus.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_map[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                temp_virus.append((nx, ny))
                temp_map[nx][ny] = 2

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                cnt += 1
    return cnt


check_load = [0 for _ in range(len(load))]
temp_wall = []


# DFS(벽을 세우는 자리 모두 확인)
def get_wall(idx, cnt):
    global result

    # 벽의 개수가 3이면 바이러스 기준으로 BFS(spread_virus())
    if cnt == 3:
        temp_map = []
        for i in matrix:  # matrix와 똑같은 행렬 하나 더 만들기
            temp_map.append(i[:])
        print(temp_wall)
        for x, y in temp_wall:  # 벽 세우기
            temp_map[x][y] = 1
        result = max(result, spread_virus(temp_map))  # 바이러스를 퍼뜨리고, 0의 갯수 찾는 spread_virus 찾기
        # pprint(result)
        return

    for i in range(idx, len(load)):
        if check_load[i] == 1:
            continue
        temp_wall.append(load[i])
        check_load[i] = 1
        get_wall(i, cnt + 1)
        temp_wall.pop()
        check_load[i] = 0


# 처음 인덱스부터 시작
get_wall(0, 0)

print(result)