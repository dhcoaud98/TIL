import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # N*N의 빈 템플릿

    # 시계방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    now = 1
    x, y = 0, 0
    d = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[x][y] = now
            x += di[d]
            y += dj[d]

            # x, y가 arr의 길이를 벗어나거나 좌표의 값이 0이 아니라면 방향전환
            if not (0 <= x < len(arr) and 0 <= y < len(arr)) or arr[x][y] != 0:
                #  두번째 for문에서 이동한 값을 제자리로 뒤로 한 칸 이동
                x -= di[d]
                y -= dj[d]
                # 방향 틀기
                d = (d + 1) % 4
                # 한 칸 이동
                x += di[d]
                y += dj[d]
            now += 1
    print(arr)


