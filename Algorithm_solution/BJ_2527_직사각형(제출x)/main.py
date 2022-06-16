import sys
sys.stdin= open('input.txt')

for tc in range(4):
    ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
    # 직사각형 a, 선분 b, 점 c, 없음 d
    # 가장 작게 사각형 만들기
    my_x = [ax, bx, cx, dx]
    max_x = max(my_x)
    my_y = [ay, by, cy, dy]
    max_y = max(my_y)
    temp = [[0]*(max_x+1) for _ in range(max_y+1)]

    for i in range(ay, by+1):
        for j in range(ax, bx+1):
            temp[i][j] += 1

    for i in range(cy, dy+1):
        for j in range(cx, dx+1):
            temp[i][j] += 1

    answer = []
    for i in range(max_y+1):
        for j in range(max_x+1):
            if temp[i][j] == 2:
                answer.append([i, j])
    # print(answer)

    result = 'a'
    cnt = 0
    # 공백?
    if len(answer) == 0:
        result = 'd'
    # 점?
    elif len(answer) == 1:
        result = 'c'
    # 선? 면?
    else:
        for k in range(len(answer)-1):
            # x값이 모두 같거나 y 값이 모두 같으면
            if answer[k][1] == answer[k+1][1]:
                cnt += 1
            elif answer[k][0] == answer[k+1][0]:
                cnt += 1
            if cnt == len(answer)-1:
                result = 'b'

    print(result)



