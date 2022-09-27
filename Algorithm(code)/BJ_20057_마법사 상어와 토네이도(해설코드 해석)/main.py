import sys
sys.stdin =open('input.txt')


N = int(input())
MATRIX = []

for _ in range(N):
    row = list(map(int, input().split()))
    MATRIX.append(row)

left_row = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
left_col = [0, -1, 0, 1, -2, -1, 0, 1, 0]
left_por = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

# left (-2, -1) -> (r, c)
# down (1, -2)  -> (-c, r)
# right (2, 1)  -> (-r, -c)
# up (-1, 2)    -> (c, -r)


def get_coords(coords, direction):
    if direction == 0:
        return coords
    elif direction == 1:
        return [-coords[1], coords[0]]
    elif direction == 2:
        return [-coords[0], -coords[1]]
    else:
        return [coords[1], -coords[0]]


start = [int(N / 2), int(N / 2)]  # (2, 2)에서 시작
direction = 0  # 좌 하 우 상
d_row = [0, 1, 0, -1]
d_col = [-1, 0, 1, 0]

walk = 1  # 토네이도가 걸어갈 길이
rlt = 0

end_flag = False

while True:
    for _ in range(walk):
        row = start[0] + d_row[direction]
        col = start[1] + d_col[direction]

        sand = 0

        for i in range(9):
            spread_coords = get_coords([left_row[i], left_col[i]], direction)
            each_row = row + spread_coords[0]
            each_col = col + spread_coords[1]
            each_sand = int(MATRIX[row][col] * left_por[i])
            sand += each_sand

            if 0 <= each_row < N and 0 <= each_col < N:
                MATRIX[each_row][each_col] += each_sand
            else:
                rlt += each_sand

        MATRIX[row][col] -= sand  # 현재 위치에 있는 모래의 값에 날아간 것 만큼 빼주기

        next_row = row + d_row[direction]
        next_col = col + d_col[direction]
        if 0 <= next_row < N and 0 <= next_col < N:
            MATRIX[next_row][next_col] += MATRIX[row][col]  # 다음 이동할 위치에 현재 내 위치의 모든 모래를 넘겨주고
        else:
            rlt += MATRIX[row][col]

        MATRIX[row][col] = 0  # 혅 내 위치의 모래는 0으로 만들기

        # 새로운 출발
        start[0] = row
        start[1] = col

        if row == 0 and col == 0:  # (0, 0)데 도달 하면 종료
            end_flag = True
            break

    if end_flag:
        break

    # 언제 더 길어지는가?
    if direction == 1 or direction == 3:
        walk += 1

    direction = (direction + 1) % 4  # 원형 큐라고 생각
 
print(rlt)