import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100) ]
    temp = []

    # 가로 합, 세로 합, 대각선합, 역 대각선 합
    my_sum_s = 0
    my_sum_rs = 0
    for i in range(100):
        my_sum_x = 0
        my_sum_y = 0
        for j in range(100):
            my_sum_x += arr[i][j]
            my_sum_y += arr[j][i]
            if i == j:
                my_sum_s += arr[i][i]
            if i+j == 99:
                my_sum_rs += arr[i][100-1-j]

        temp.append(my_sum_x)
        temp.append(my_sum_y)
    temp.append(my_sum_s)
    temp.append(my_sum_rs)

    # 최댓값 구하기
    max_num = 0
    for t in temp:
        if t >= max_num:
            max_num = t

    print(f'#{tc} {max_num}')