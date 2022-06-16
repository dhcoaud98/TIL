import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # 오류 방지를 위해서 각 행의 맨 앞과 뒤에 0을 추가
    temp = [[0]*100 for _ in range(100)]
    dy = [0, 1, 0, -1]  # 상하
    dx = [1, 0, -1, 0]  # 좌우

    # 1. 마지막 지점이 2인 부분을 찾기
    for i in range(101):  # 범위가 range(101)인 이유는 앞 뒤로 0을 추가 해주었기 때문에 전체 행의 길이가 2개 늘어났기 때문이다.
        if arr[99][i] == 2:
            end = i

    # 2. arr[98][end]부터 올라가기
    now_y = 98
    now_x = end
    while now_y > 0:  # 첫번째 행에 도착하면 종료
        if arr[now_y][now_x+1] == 1:  # 오른쪽으로 꺽기
            now_x += 1
            # 오른쪽으로 계속 움직이기, 움직이는 방향에서 값이 0이 나오면 중단 하고 위로 움직이기
            while arr[now_y][now_x+1] != 0:
                now_x += 1
            now_y += -1
        elif arr[now_y][now_x-1] == 1:  # 왼쪽으로 꺽기
            now_x += -1
            # 왼쪽으로 계속 움직이기, 움직이는 방향에서 값이 0이 나오면 중단하고 위로 움직이기
            while arr[now_y][now_x-1] != 0:
                now_x += -1
            now_y += -1
        else:  # 좌우로 꺽지 않으면 위로 계속 직진하기
            now_y += -1

    print(f'#{tc} {now_x-1}')





