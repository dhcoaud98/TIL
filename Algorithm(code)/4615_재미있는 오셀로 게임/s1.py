import sys
sys.stdin= open('sample_input(1).txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    basic = [[0]*(N+1)]+[[0]*(N+1) for _ in range(N)]

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    # 1. 기본 오셀로판 만들기
    for i in range(N//2, (N//2)+2):
        for j in range(N//2, (N//2)+2):
            if i == j:
                basic[i][j] = 2
            else:
                basic[i][j] = 1

    # 2. 게임 진행
    for m in range(M):
        y, x, a = map(int, input().split())

        # if a == 1:
        #     color = 'B'
        #     change = 'W'
        # else:
        #     color = 'W'
        #     change = 'B'

        basic[y][x] = a
        # print(basic)
        
        # 탐색
        for k in range(8):  # 12시부터 시계방향으로 돌기!
            s = []
            for l in range(1, N+1):
                nx = x + dx[k]*l
                ny = y + dy[k]*l
                if 1 <= nx <N+1 and 1 <= ny < N+1:  # 범위 이내에 돌고
                    if basic[ny][nx] == 0:
                        break
                    elif basic[ny][nx] == a:  # 나랑 같으면?
                        for ci, cj in s:
                            basic[ci][cj] = a
                        break
                    else:  # 같지 않다면 s에 저장
                        s.append((ny, nx))
                else:
                    break
        # print(basic)

    bcnt = wcnt = 0
    for lst in basic:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')