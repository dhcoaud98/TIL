import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

def load():
    global stack, visited, result, x, y

    while stack:  # false일 때까지 돌리기
        # start 지점에서 0인 방향으로 움직이기
        p = stack.pop()
        if p not in visited:  # 아직 방문하지 않은 곳이라면
            visited.append(p)
            for k in range(4):
                if 0 <= p[0] + dx[k] < N and 0 <= p[1] + dy[k] < N:
                    if arr[p[0] + dx[k]][p[1] + dy[k]] == 2:  # 도착한 곳이 2라면 종료
                        result = 1
                        print(f'#{tc} 1')
                    elif arr[p[0] + dx[k]][p[1] + dy[k]] == 0:
                        stack.append([p[0] + dx[k], p[1] + dy[k]])
    if result == 0:
        print(f'#{tc} 0')


# 메인
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 방향벡터 사용
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    # 2와 3인 지점의 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                x = i
                y = j


    # 현재좌표는 start[0], start[1]
    # [0, 1]
    result = 0
    stack =[[x, y]]
    visited = []
    load()


