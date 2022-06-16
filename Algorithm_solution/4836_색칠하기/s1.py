import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    draw_cnt = int(input())
    temp = [[0]*10 for _ in range(10)]

    cnt = 0
    c = []
    # 1. 색칠할 때마다 +1 하기
    for i in range(draw_cnt):
        color = list(map(int, input().split()))

        start_x = color[0]
        start_y = color[1]
        end_x = color[2]
        end_y = color[3]
        now_color = color[4]

        # 좌에서 우로 칠하면서 상에서 하로 움직여준다.
        for j in range(end_y-start_y+1):
            now_x = color[0]
            now_y = start_y
            for k in range(end_x-start_x+1):
                temp[now_x][now_y] += 1
                now_x += 1

            start_y += 1
        c.append(now_color)  # [1, 2]

    # 2. 색칠된 공간에 값이 2 이상인 갯수를 출력
    for i in range(10):
        for j in range(10):
            if 1 in c and 2 in c and temp[i][j] >= 2:  # 컬러가 1과 2가 동시에 있고, 횟수가 2가 넘을 경우
                cnt += 1
                
    print(f'#{tc} {cnt}')
