import sys
sys.stdin = open('input.txt')
T = int(input())

# 테이블에서 1은 코어를, 2는 전선을 의미
def DFS(order, core):
    global table, cnt, N, result
    if order == S:
        # 만일 모든 코어에서 연결을 시도한 후 해당 코어가 최대 개수가 아니거나 최대 개수와 같지만 연결이 길다면 결과에 반영하지 않음
        if core < result[0] or (core == result[0] and cnt >= result[1]):
            return
        else:
            result = (core, cnt)
    else:
        if start_point[order][0] == 1 or start_point[order][0] == N or start_point[order][1] == 1 or start_point[order][1] == N:
            DFS(order+1, core+1)
        else:
            flag = 0
            for k in range(4):  # 4방향을 탐색함
                x = start_point[order][0]
                y = start_point[order][1]
                while table[x+dx[k]][y+dy[k]] != 'p':  # 전선이나 코어로 막혀있는 경우구하기
                    x += dx[k]
                    y += dy[k]
                    if table[x][y] == 1 or table[x][y] == 2:
                        flag += 1
                        break
                else:  # 전선이나 코어가 없는 경우 -> 테이블에 전선을 놓기(2)로 만들기
                    x = start_point[order][0]
                    y = start_point[order][1]
                    while table[x+dx[k]][y+dy[k]] != 'p':
                        x += dx[k]
                        y += dy[k]
                        table[x][y] = 2
                        cnt += 1
                    DFS(order+1, core+1)
                    while table[x][y] != 1:  # return 후 돌아오면 더이상 진행하지 못하고 방향을 바꿔야 하므로 지나왔던 길을 0으로 리셋.
                        table[x][y] = 0
                        cnt -= 1
                        x -= dx[k]
                        y -= dy[k]
            if flag == 4:  # flag가 4라는 것은, 상/하/좌/우 모두 연결할 수 없다는 것.
                DFS(order+1, core)  # 그러므로 core를 세주지 않는다

for tc in range(1, T+1):
    N = int(input())
    table = [['p'] * (N+2)] + list(['p'] + list(map(int, input().split())) + ['p'] for _ in range(N)) + [['p'] * (N+2)]
    start_point = []
    result = (0, N**2)  # (연결된 코어 개수, 전선의 길이). (0, N**2)로 초기화하여
    cnt = 0             # DFS의 첫 결과부터 result에 반영되도록 설정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # print(table)
    # 시작점 등록하기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if table[i][j] == 1:
                start_point.append((i, j))
    # print(start_point)
    S = len(start_point)
    # print(S)

    DFS(0, 0)

    print(f'#{tc} {result[1]}')