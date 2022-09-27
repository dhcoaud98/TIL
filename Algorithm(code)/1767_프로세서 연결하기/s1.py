import sys
sys.stdin = open('input.txt')

def DFS(process, core):
    """
    :param process: 순차적으로 다음 process에서 함수를 돌리기 위해 진행함
    :param core: 현재 연결 된 core 갯수
    :return: 
    """
    global total, result, now, cnt

    if process == total:  # 마지막 프로세스에 도달했을 때
        # 연결된 갯수가 제일 처음 계산한 값보다 작거나/ 연결된 갯수는 같지만 전선의 수가 많을땐 return
        if core < result[0] or (core == result[0] and cnt >= result[1]):
            return
        else:
            result = [core, cnt]

    else:  # 마지막 프로세스가 아니라면 계속 해서 진행해주기
        x = now[process][1]
        y = now[process][0]
        if x == 0 or x == N-1 or y == 0 or y == N-1:  # 가장 자리라면?
            DFS(process+1, core+1)
        else:  # 가장 자리가 아니라면?
            stop = 0
            for k in range(4):
                x = now[process][1]
                y = now[process][0]
                while 0 <= y+dy[k] < N and 0 <= x+dx[k] < N:  # 전체 범위 안에서 막힌 부분 찾기
                    x += dx[k]
                    y += dy[k]
                    if arr[y][x] == 1 or arr[y][x] == 2:
                        stop += 1
                        break
                else:  # while 문을 break문 없이 통과하여 한 방향으로 막힘이 없다면 전선을 연결하기
                    x = now[process][1]
                    y = now[process][0]
                    while 0 <= y+dy[k] < N and 0 <= x+dx[k] < N:
                        x += dx[k]
                        y += dy[k]
                        arr[y][x] = 2
                        cnt += 1
                    DFS(process+1, core+1)
                    while arr[y][x] != 1:  # return 받아서 while문 실행하면 프로세서 있는 위치 까지 reset하기
                        arr[y][x] = 0
                        x -= dx[k]
                        y -= dy[k]
                        cnt -= 1
            if stop == 4:
                DFS(process+1, core)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    total = 0
    now = []
    cnt = 0
    result = [0, N*N]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                total += 1
                now.append([i, j])

    DFS(0, 0)
    print(f'#{tc} {result[1]}')
