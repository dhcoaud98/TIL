import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # 0번째 행에서 1이 있는 위치 모두 찾아서 list로 만들기
    ONES = []
    for i in range(102):
        if arr[0][i]:
            ONES.append(i)

    # [1, 4, 13, 19, 21, 32, 38, 48, 58, 62, 68, 75, 82, 85, 94, 97, 100]
    answer = []
    min_cnt = 100*100
    for one in ONES:
        cnt = 1
        now_x = one
        now_y = 1
        while now_y < 100:
            # 오른쪽으로 꺽기
            if arr[now_y][now_x+1] == 1:
                now_x += 1
                cnt += 1
                while arr[now_y][now_x + 1] == 1:  # 오른쪽에 길이 있다면 계속 가라.
                    now_x += 1
                    cnt += 1
                now_y += 1
                cnt += 1
            # 왼쪽으로 꺽기
            elif arr[now_y][now_x-1] == 1:
                now_x -= 1
                cnt += 1
                while arr[now_y][now_x-1] == 1:  # 왼쪽에 길이 있다면 계속 가라.
                    now_x -= 1
                    cnt += 1
                now_y += 1
                cnt += 1
            # 둘다 아니면 위로 가기
            else:
                now_y += 1
                cnt += 1
        if cnt <= min_cnt:
            min_cnt = cnt
        answer.append([one, now_x, cnt])

    for i in range(len(answer)):
        if answer[i][2] == min_cnt:
            print(f'#{tc} {answer[i][0]-1}')


                



